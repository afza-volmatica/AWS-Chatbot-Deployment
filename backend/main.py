from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

from ollama_service import get_llm_response

app = FastAPI(
    title="Ollama Chatbot API",
    version="1.0.0"
)

# CORS Configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # For development
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class ChatRequest(BaseModel):
    message: str


class ChatResponse(BaseModel):
    response: str

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/")
def health_check():
    return {
        "status": "running",
        "message": "Chatbot API is healthy"
    }


@app.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
    bot_response = get_llm_response(request.message)

    return ChatResponse(
        response=bot_response
    )