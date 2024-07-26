from fastapi import FastAPI, HTTPException, Request
import httpx
import os

app = FastAPI()

OPENAI_API_KEY = os.getenv("DEEPSEEK_API_KEY")
OPENAI_API_URL = "https://api.deepseek.com/v1"


async def forward_request(request: Request, endpoint: str):
    async with httpx.AsyncClient() as client:
        headers = {
            "Authorization": f"Bearer {OPENAI_API_KEY}",
            "Content-Type": "application/json"
        }
        body = await request.json()
        response = await client.post(f"{OPENAI_API_URL}/{endpoint}", json=body, headers=headers)
        if response.status_code != 200:
            raise HTTPException(status_code=response.status_code, detail=response.text)
        return response.json()

@app.post("/v1/chat/completions")
async def chat_completions(request: Request):
    return await forward_request(request, "chat/completions")

@app.post("/v1/completions")
async def completions(request: Request):
    return await forward_request(request, "completions")

@app.post("/v1/edits")
async def edits(request: Request):
    return await forward_request(request, "edits")

@app.post("/v1/embeddings")
async def embeddings(request: Request):
    return await forward_request(request, "embeddings")

@app.post("/v1/audio/transcriptions")
async def audio_transcriptions(request: Request):
    return await forward_request(request, "audio/transcriptions")

@app.post("/v1/audio/translations")
async def audio_translations(request: Request):
    return await forward_request(request, "audio/translations")

@app.get("/v1/models")
async def models():
    async with httpx.AsyncClient() as client:
        headers = {
            "Authorization": f"Bearer {OPENAI_API_KEY}"
        }
        response = await client.get(f"{OPENAI_API_URL}/models", headers=headers)
        if response.status_code != 200:
            raise HTTPException(status_code=response.status_code, detail=response.text)
        return response.json()

@app.get("/v1/models/{model}")
async def model(model: str):
    async with httpx.AsyncClient() as client:
        headers = {
            "Authorization": f"Bearer {OPENAI_API_KEY}"
        }
        response = await client.get(f"{OPENAI_API_URL}/models/{model}", headers=headers)
        if response.status_code != 200:
            raise HTTPException(status_code=response.status_code, detail=response.text)
        return response.json()


