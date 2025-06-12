from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import uvicorn

app = FastAPI()

@app.get("/")
async def root():
    return {
        "message": "RAG Chatbot API is running",
        "version": "1.0.0",
        "status": "ready"
    }

@app.post("/chat")
async def chat(request: Request):
    body = await request.json()
    query = body.get("query")
    
    # Dummy response (aap yahan apna actual RAG logic daal sakte ho baad mein)
    return {"answer": f"You asked: '{query}'. This is a demo response from your RAG Chatbot."}
