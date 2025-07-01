# 🧠 Agentic RAG Medical Assistant

Asistente médico inteligente basado en un modelo **LLaMA 3.1 8B fine-tuned**, potenciado con un pipeline **RAG con agentes** para consultas clínicas, documentación médica y recomendaciones personalizadas.

---

## 🔍 Características

- **📚 RAG con 20+ fuentes médicas**: Recuperación de información médica actualizada y relevante.
- **🧠 LLM Fine-tuned**: Modelo LLaMA 3.1 (8B) entrenado con **LoRA** y acelerado con **Unsloth 4-bit**, logrando un **ROUGE1 score de 0.29**.
- **🗂️ Integración FHIR**: Soporte para lectura de historiales clínicos desde servidores **FHIR R4**, compatible con sistemas EHR.
- **🤖 Agentes inteligentes**:
  - Detectan si una consulta es médica o no.
  - Enrutan automáticamente: RAG para consultas clínicas, Wikipedia para otras.
- **⚡ Interfaz rápida**: Chat asíncrono con **FastAPI**, latencia reducida en un **40%**.

---

## 🧰 Tech Stack

| Componente     | Tecnología                                        |
|----------------|---------------------------------------------------|
| 🔗 LLM         | LLaMA 3.1 8B + PEFT (LoRA) + GGUF (HF)            |
| 🧪 RAG         | LangChain + ChromaDB                              |
| 🏥 EHR         | FHIR R4 API (mediante `fhir.resources`, `httpx`)  |
| 🌐 Backend     | FastAPI (asynchronous API + Web UI)               |
| 📦 Inference   | Ollama + Unsloth                                   |

---

## ⚙️ Instalación Rápida

1. **Clona el repositorio**
   ```bash
   git clone https://github.com/SathvikNayak123/Agentic-RAG.git
   cd Agentic-RAG

2. **Instala dependencias**
pip install -r requirements.txt

3. **Descarga el modelo**
ollama pull hf.co/sathvik123/llama3-ChatDoc

4. **Carga documentos y genera embeddings**
python ingest.py

5. **Inicia la app**
uvicorn app:app --reload
