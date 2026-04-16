from pathlib import Path

from fastapi import FastAPI
from pydantic import BaseModel

from config.settings import settings
from core.agent_runner import AgentRunner

app = FastAPI(title="Custom Agent Starter", version="0.1.0")
project_root = Path(__file__).resolve().parents[2]
runner = AgentRunner(project_root=project_root)


class ChatRequest(BaseModel):
    message: str


@app.get("/health")
def health() -> dict:
    return {
        "status": "ok",
        "provider": settings.model_provider,
        "model": settings.model_name,
    }


@app.post("/chat")
def chat(req: ChatRequest) -> dict:
    response = runner.run(req.message)
    return {
        "provider": settings.model_provider,
        "model": settings.model_name,
        "response": response,
    }
