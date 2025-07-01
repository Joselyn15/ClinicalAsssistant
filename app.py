# app.py
from fastapi import FastAPI, HTTPException, Request, Body
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from RAG.rag import RAG_chatbot

bot = RAG_chatbot()        # instancia global
app = FastAPI()
templates = Jinja2Templates(directory="templates")

class UserQuery(BaseModel):
    user_query: str
    patient_id: str | None = None  

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/chat")
async def chat_endpoint(payload: UserQuery = Body(...)):
    try:
        answer = await bot.get_response(
            payload.user_query,
            payload.patient_id              # 🔸 lo enviamos al bot
        )
        return {"answer": answer}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))