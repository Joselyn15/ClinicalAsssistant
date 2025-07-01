# Resumen del sistema:
"Este asistente clínico combina datos estructurados (FHIR, HL7, FDA) y contexto no estructurado (PDFs médicos) usando un enfoque RAG para responder preguntas médicas de forma personalizada. El flujo está orquestado por una clase RAG_chatbot que gestiona la obtención de datos clínicos, análisis de síntomas con un LLM, y recuperación de contexto relevante para generar respuestas confiables."

# Arquitectura de componentes (puedes hacer un diagrama con draw.io o usar texto):

- FastAPI para endpoints

- HTML/CSS para UI básica

- Ollama LLM (modelo Gemma ) para RAG

- Módulo RAG_chatbot como orquestador

- Servicios: fhir_safe, hl7_client, fda_safe, ai_safe

- Vector store con ChromaDB

- Embeddings: MiniLM

- Historial de sesión para contextualización

# Decisiones técnicas importantes:
Uso de modelos open-source por privacidad

Modularización con services/ para pruebas unitarias

FHIR y HL7 simulados pero con endpoints válidos

Prompt engineering con ChatPromptTemplate