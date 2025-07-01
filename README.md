# Agentic RAG Medical Assistant

Asistente médico inteligente basado en un modelo LLaMA 3.1 8B fine-tuned, potenciado con un pipeline RAG con agentes, para consultas clínicas, documentación médica y recomendaciones personalizadas.

## Características

- RAG con más de 20 fuentes médicas: recuperación de información médica actualizada y relevante.
- LLM Fine-tuned: Modelo LLaMA 3.1 (8B) entrenado con LoRA y acelerado con Unsloth 4-bit, logrando un ROUGE1 score de 0.29.
- Integración FHIR: Soporte para lectura de historiales clínicos simulados desde servidores FHIR R4.
- Procesamiento HL7: Soporte para parsing de mensajes del sistema de laboratorio (formato HL7 v2).
- Análisis de síntomas: El agente genera códigos ICD-10 sugeridos para síntomas ingresados en lenguaje natural.
- Generación multilingüe: El modelo detecta el idioma (español/inglés) y responde automáticamente en el idioma correspondiente.
- Agente coordinador clínico: `OncologyCoordinator` integra todas las fuentes (FHIR, HL7, FDA, RAG, LLM).
- Enrutamiento inteligente: Detecta si una consulta es médica y utiliza RAG para salud, Wikipedia para otras consultas.
- Selección de paciente: Menú desplegable en la interfaz para elegir entre múltiples pacientes simulados.
- Interfaz rápida: Chat web con FastAPI + Bootstrap, con latencia reducida.

## Tech Stack

| Componente   | Tecnología                              |
|--------------|------------------------------------------|
| LLM          | LLaMA 3.1 8B + LoRA + GGUF + Unsloth     |
| RAG          | LangChain + ChromaDB                    |
| EHR          | FHIR R4 API (fhir.resources, httpx)      |
| HL7          | hl7.parser (stream de laboratorio)       |
| Interacciones| OpenFDA API (limitada a 10 req/min)      |
| Backend      | FastAPI (endpoints asíncronos + Web UI)  |
| Frontend     | Bootstrap + JS Fetch API                 |
| Coordinador  | `OncologyCoordinator()` (agente maestro) |
| Inference    | Ollama + Unsloth 4-bit                   |

## Instalación Rápida

```bash
# Clonar el repositorio
git clone https://github.com/SathvikNayak123/Agentic-RAG.git
cd Agentic-RAG

# Instalar dependencias
pip install -r requirements.txt

# Descargar el modelo
ollama pull hf.co/sathvik123/llama3-ChatDoc

# Ingestar documentos y generar embeddings
python ingest.py

# Iniciar la aplicación
cd ClinicalAssistant
uvicorn app:app --reload
