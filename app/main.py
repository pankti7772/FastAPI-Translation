from fastapi import FastAPI, HTTPException
from app.schemas import TranslationRequest, TranslationResponse
from app.model import translation_model

app = FastAPI(
    title="Language Translation Service",
    description="A microservice to translate English text to French using a Transformer model.",
    version="1.0.0"
)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Language Translation API. Visit /docs for Swagger UI."}

@app.get("/translate")
def translate_info():
    return {"message": "This endpoint accepts only POST requests. Please use the Swagger UI at /docs or a tool like 'curl' or 'test_request.py' to send a POST request with JSON body."}

@app.post("/translate", response_model=TranslationResponse)
def translate_text(request: TranslationRequest):
    try:
        translated = translation_model.translate(request.text)
        return TranslationResponse(
            original_text=request.text,
            translated_text=translated
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
