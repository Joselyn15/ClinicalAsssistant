# Agentic RAG Medical Assistant

Asistente médico basado en lenguaje natural para consultas clínicas simuladas. Utiliza una arquitectura modular que integra FHIR, procesamiento HL7 y un modelo LLM multilingüe con un sistema de agentes básicos.

## ✅ ¿Qué incluye esta versión?

- Interfaz web funcional con FastAPI + Bootstrap.
- Selector de paciente desde un menú desplegable.
- Endpoint `/chat` funcional que enruta preguntas al LLM.
- Implementación básica del agente `OncologyCoordinator` con integración de:
  - FHIR simulado (`patient_context`)
  - Parsing de mensajes HL7 simulados (`hl7_context`)
  - Análisis de síntomas básicos (`symptoms_analysis`)
- Generación de respuestas automáticas en español o inglés, según el idioma de la pregunta.
- LLM conectado vía Ollama u otro proveedor local.

## ⚠️ Limitaciones actuales

- No se finalizó la demo completamente integrada (flujo clínico automático aún incompleto).
- Algunas funcionalidades (ej. FDA API o análisis profundo de interacciones) están simuladas o pendientes de integración.
- El sistema RAG funciona sobre documentos locales pero no se completó la capa de recuperación multifuente ni embeddings finales.
- Algunos errores aún presentes en el flujo completo (respuesta inconsistente del LLM o múltiples salidas por mensaje).

## Tech Stack usado

| Componente   | Tecnología                            |
|--------------|----------------------------------------|
| LLM          | Ollama local (modelo tipo LLaMA)       |
| Agentes      | `OncologyCoordinator()` coordinador clínico |
| EHR Simulado | FHIR R4 (`fhir.resources`)             |
| HL7 Parsing  | `hl7.parser` en modo lectura básica     |
| Backend API  | FastAPI                               |
| Frontend     | HTML + Bootstrap + JavaScript (Fetch) |

##  Próximos pasos
Finalizar integración completa entre agentes y fuentes de datos estructurados.

Implementar validación de síntomas con ICD-10 desde entrada libre.

Mejorar la precisión multilingüe del LLM para respuestas más naturales.

Agregar manejo de contexto clínico longitudinal y resumen automático.

## Instalación Básica

```bash
# Clonar este repositorio
git clone https://github.com/Joselyn15/ClinicalAsssistant.git
cd ClinicalAsssistant

# Instalar dependencias
pip install -r requirements.txt

# Iniciar el servidor
uvicorn app:app --reload
