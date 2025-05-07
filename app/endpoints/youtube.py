import os
from fastapi import APIRouter, Query
from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled, NoTranscriptFound

router = APIRouter()

PROXY_URL = os.getenv("PROXY_URL")  # pega do ambiente
proxies = {"http": PROXY_URL, "https": PROXY_URL} if PROXY_URL else None

@router.get("/transcript")
def get_transcript(video_id: str = Query(..., description="ID do vídeo YouTube"),
                   lang: str = Query("pt,en,es", description="Idiomas preferidos separados por vírgula")):
    try:
        langs = [l.strip() for l in lang.split(",")]
        transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=langs, proxies=proxies)
        return {
            "video_id": video_id,
            "languages": langs,
            "segments": transcript
        }
    except TranscriptsDisabled:
        return {"error": "Transcrições desativadas para este vídeo."}
    except NoTranscriptFound:
        return {"error": "Nenhuma transcrição encontrada para os idiomas fornecidos."}
    except Exception as e:
        return {"error": str(e)}

