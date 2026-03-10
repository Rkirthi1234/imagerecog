from fastapi import FastAPI, UploadFile, File, Query
from app.model import generate_caption
from app.generator import generate_creative_text, generate_all_styles
from app.utils import load_image
from app.schemas import PredictionResponse, AllStylesResponse

app = FastAPI(title="Image Recognition API")

# Simple in-memory cache: caption -> creative text per style
_cache: dict = {}


@app.post("/predict", response_model=PredictionResponse)
async def predict(
    file: UploadFile = File(...),
    style: str = Query(default="vivid", enum=["vivid", "Artistic", "Cinematic", "Playful"]),
):
    image = load_image(file.file)

    caption_result = generate_caption(image)
    best_caption = caption_result["best_caption"]

    cache_key = f"{best_caption}::{style}"
    if cache_key not in _cache:
        _cache[cache_key] = generate_creative_text(best_caption, style)

    return {
        "caption": caption_result,
        "creative_text": _cache[cache_key],
    }


@app.post("/predict/all-styles", response_model=AllStylesResponse)
async def predict_all_styles(file: UploadFile = File(...)):

    image = load_image(file.file)

    caption_result = generate_caption(image)
    best_caption = caption_result["best_caption"]

    styles_result = generate_all_styles(best_caption)

    return {
        "caption": caption_result,
        "styles": styles_result,
    }


@app.get("/styles")
def list_styles():
    return {
        "styles": ["vivid", "Artistic", "Cinematic", "Playful"],
        "default": "vivid",
    }