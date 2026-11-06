from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, ValidationError
from model_backend import FakeModelBackend, ModelRequest

class GenerateRequest(BaseModel):
    request_id: str
    prompt: str

app = FastAPI()


@app.get("/healthz")
def healthz():
    return {"status":"ok"}


@app.post("/v1/generate")
def generateRequest(request: GenerateRequest):
    backend = FakeModelBackend(reply_text="Scan requested.")
    try:
        response = backend.generate(ModelRequest(request_id=request.request_id, prompt=request.prompt))
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    return response