# Enhanced RAG Chatbot

Versión robusta del chatbot de **Retrieval-Augmented Generation (RAG)** para entornos clínicos demo.  
Incluye tolerancia a fallos, parsing HL7 de alto volumen y caché en memoria.

## 1. Características principales
| Módulo | Descripción breve |
|--------|-------------------|
| **CircuitBreaker** | Aísla al sistema si el servicio FHIR empieza a fallar (umbral y timeout configurables). |
| **RobustHL7Handler** | Parser tolerante (v2.3/v2.5) con buffer circular y agregación de labs por paciente. |
| **ResponseCache** | Caché LRU (~1 000 entradas, TTL 30 min) para acelerar consultas repetidas. |
| **StateGraph (LangGraph)** | Pipeline declarativo: `validate → retrieve → patient_context → answer → END`. |
| **Fallbacks multinivel** | Cache → Ollama LLM → Respuesta simplificada, nunca se cae. |
| **Métricas en tiempo real** | `get_system_status()` expone KPIs para dashboards externos. |
| **Simulación HL7** | `simulate_hl7_stream()` genera tráfico sintético para pruebas de rendimiento. |

## 2. Requisitos

| Dependencia | Versión sugerida |
|-------------|------------------|
| Python | 3.11+ |
| `langchain`, `langgraph` | ≥ 0.1 |
| `chroma` | ≥ 0.4 |
| `sentence-transformers` | ≥ 2.2 |
| `ollama` servidor local | Modelo `llama3-ChatDoc` |
| (Opcional) Groq API | Variable `GROQ_API_KEY` si quieres cambiarla |

Instala todo con:

```bash
pip install -r requirements.txt

---------------------

| Área                  | Factible (< 24 h)                                      | Requiere más tiempo                            |
| --------------------- | ------------------------------------------------------ | ---------------------------------------------- |
| **HL7 ingest**        | Ingestar a Kafka/Redis stream .         | Normalización completa HL7 v2.x, mapping FHIR. |
| **FHIR resiliente**   | Token refresh + xml→json fallback (`xmltodict.parse`). | Unificación de 5 EHR en FHIR-mapper.           |
| **Rate-limit mgmt.**  | Token-bucket + cache LRU (simple).                     | Monitoreo dinámico + auto-scaling workers.     |
| **AI síntomas**       | Usa wrapper SafeClient + re-intentos.                  | Consistencia LLM (reinforcement feedback).     |
| **Cross-modal score** | Heurística rápida (umbral labs + síntomas).            | Modelo ML/graph basado en histórico.           |
| **Seguridad**         | `.env` + vault para credenciales.                      | IAM granular + logging PHI compliant.          |
