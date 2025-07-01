import asyncio
from RAG.rag import RAG_chatbot

async def main():
    bot = RAG_chatbot()
    respuesta = await bot.get_response(
        "¿Es adecuado su tratamiento con el nivel actual de hemoglobina?",
        patient_id="paciente-1"
    )
    print("→", respuesta)

if __name__ == "__main__":
    asyncio.run(main())