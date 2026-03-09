from fastapi import FastAPI, UploadFile, File
from app.model import generate_caption
from app.generator import generate_creative_text
from app.utils import load_image

app = FastAPI(title="Image Recognition API")


@app.post("/predict")
async def predict(file: UploadFile = File(...)):

    image = load_image(file.file)

    caption = generate_caption(image)

    creative_text = generate_creative_text(caption)

    return {
        "caption": caption,
        "creative_text": creative_text
    }