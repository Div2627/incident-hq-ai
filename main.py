from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from pydantic import BaseModel
from swarm_orchestrator import execute_swarm_pipeline
from mock_data import MOCK_INCIDENT_LOG

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatMessage(BaseModel):
    message: str

@app.get("/")
async def read_index():
    return FileResponse('index.html')

@app.post("/api/trigger-swarm")
async def trigger_swarm():
    timeline = execute_swarm_pipeline(MOCK_INCIDENT_LOG)
    return {"status": "resolved", "timeline": timeline}

@app.post("/api/chat")
async def chat_with_agent(payload: ChatMessage):
    user_msg = payload.message.lower()
    
    # Context-aware deterministic command responses
    if "status" in user_msg or "incident" in user_msg:
        return {"response": "🤖 [System Monitor] Incident ID #4092 state is currently set to RESOLVED. The connection pool has dropped back to stable thresholds (4/100 active)."}
    elif "why" in user_msg or "approve" in user_msg:
        return {"response": "🛡️ [QA Inspector Agent] I approved the patch because the explicit 'finally' block ensures connection closure even if runtime network anomalies occur. Syntax parsing matches Python AST standards."}
    elif "rollback" in user_msg:
        return {"response": "🔄 [Swarm Triager] Rollback sequence initialized. Reverting to backup code commit v2.4.11. Monitoring telemetry for anomalies."}
    
    return {"response": f"💬 [IncidentHQ Core] Roger that. Command received. Running background validation protocols for: '{payload.message}'."}