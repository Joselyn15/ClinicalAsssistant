# README - Plan de Producción para Asistente Clínico IA

## Contexto Real del Centro Oncológico

El equipo de ingeniería visitó el centro oncológico y recopiló los siguientes desafíos técnicos y operativos:

### Realidad del Sistema

* 5 sistemas EHR no interoperables.
* 12+ apps/dispositivos usados por pacientes.
* Fuentes de datos heterogéneas: notas clínicas, laboratorios, wearables, PROs.
* Enfermeras gastan 40% del tiempo en tareas administrativas.
* Oncólogos no pueden identificar a tiempo a pacientes de alto riesgo.

### Problemas Técnicos Detectados

* HL7: >1000 msgs/min en horas pico. Malformaciones, codificación, versiones mixtas.
* FHIR: retorna XML, IDs duplicados, autenticación inestable.
* FDA API: caché obsoleto, límite de 10 req/min.
* Clinical AI: respuestas inconsistentes, context window limitado, 15% de fallos por red.
* Conexiones se caen cada 2h por políticas IT.

### Restricciones de Seguridad

* No almacenar PHI en nube.
* Todo acceso debe pasar por proxy institucional.
* Logs de auditoría obligatorios.

## Enfoque de Solución Priorizado

| Prioridad | Tarea Clave                                               | Justificación                            |
| --------- | --------------------------------------------------------- | ---------------------------------------- |
| **P0**    | Procesamiento de HL7 en tiempo real + tolerancia a fallos | Alto volumen y criticidad de laboratorio |
| **P0**    | Safe Clients con retry y logging (FHIR, FDA, AI)          | Latencia, caídas, cumplimiento HIPAA     |
| **P0**    | UI con soporte español + accesibilidad                    | 55% de pacientes en riesgo digital       |
| **P1**    | Desduplicación y normalización FHIR                       | Datos ruidosos y duplicados              |
| **P1**    | Cache control y verificación FDA                          | Respuestas obsoletas                     |
| **P1**    | Auditoría: logs trazables por cada acceso                 | Requisito legal                          |
| **P2**    | Evaluación de confianza del LLM + explicación             | Para uso clínico seguro                  |
| **P2**    | Expansión de base de conocimiento RAG oncológico          | Mejora respuestas clínicas               |

## 🔧 Componentes de Código Agregados

* `services/fhir_safe.py`: manejo robusto de FHIR (XML → JSON, retry, logging).
* `services/fda_safe.py`: cache-aware con retry e identificación de data vieja.
* `services/ai_safe.py`: manejo de rate limit + fallos del modelo LLM.
* `utils/rate_clients.py`: decoradores de retry/backoff y auditoría.
* `hl7_stream_consumer.py`: procesamiento en vivo con buffer y validación.

## Respuesta al Escenario de Producción

- Se eliminó cualquier almacenamiento de PHI en la nube (solo procesamos en memoria).
- Todos los endpoints (FHIR, HL7, FDA, AI) se enrutan a través del proxy con latencia simulada.
- SafeClients implementan retry, timeout, logging y control de tasa.
- Sistema tolera caídas con buffer circular (HL7) y recuperación automática.
- UI accesible para adultos mayores y traducción español-inglés integrada.
- Se usan datos sintéticos + logs auditables para demo clínica confiable.

## 🗺️ Roadmap 90 Días (Piloto)

| Semana | Entregable                                              | Estado |
| ------ | ------------------------------------------------------- | ------ |
| 1      | MVP Chatbot + HL7 Realtime + UI básica accesible        | ✅      |
| 2–3    | Logging/Auditoría + Retry safe clients                  | 🔄     |
| 4–5    | Test con datos sintéticos + revisión clínica            | ⏳      |
| 6–7    | Evaluación de confianza del modelo (consistency + SHAP) | ⏳      |
| 8–9    | RAG Expansion + FHIR deduplication                      | ⏳      |
| 10     | Demo final + métricas clínicas y técnica                | ⏳      |

## Métricas de Éxito (KPI **objetivos** del piloto)

> **Nota:** Las cifras de la tabla son metas a alcanzar durante el piloto de 90 días; no representan resultados actuales. Se validarán con los datos sintéticos primero y, de ser aprobados, con PHI real en fase 2.

| Métrica                        | Objetivo                                                | Cómo se medirá                                                   |
| ------------------------------ | ------------------------------------------------------- | ---------------------------------------------------------------- |
| Latencia promedio de respuesta | **< 100 ms**                                            | Prometheus + Grafana (p95 y p50)                                 |
| Resiliencia a caídas           | **Recovery automático ≤ 30 s**, 0 mensajes HL7 perdidos | Tests de desconexión cada 2 h (Chaos Monkey)                     |
| Satisfacción usuario clínico   | **≥ 85 %** en encuesta (SUS)                            | Survey a oncólogos/enfermeras al día 30 y 60                     |
| Insights clínicos relevantes   | **≥ 3** por paciente / piloto                           | Revisión manual de 10 historiales sintéticos por oncólogo senior |
| Precisión respuestas RAG       | **≥ 90 %** relevancia top‑3                             | Doble revisión ciega por 2 oncólogos                             |

## Riesgos

* Fallos del Clinical AI en casos límite
* Proxy institucional aumenta latencia
* Datos anónimos no reflejan toda la complejidad

---

*Actualizado el 1 de julio de 2025 — Equipo IA Clínica Oncológica*

¿Preguntas? Contactar a: `ai-team@oncology-demo.org`