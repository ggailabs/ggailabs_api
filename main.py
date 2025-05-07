from fastapi import FastAPI
from app.endpoints import youtube

app = FastAPI(
    title="GG.AI Labs API Hub",
    description="API com múltiplos endpoints para automações e integrações",
    version="1.0.0"
)

# Inclua aqui seus endpoints
app.include_router(youtube.router, prefix="/youtube", tags=["YouTube"])
