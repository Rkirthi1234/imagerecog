import torch
from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image

device = "cuda" if torch.cuda.is_available() else "cpu"

processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-large")
model = BlipForConditionalGeneration.from_pretrained(
    "Salesforce/blip-image-captioning-large",
    torch_dtype=torch.float16 if device == "cuda" else torch.float32,
).to(device)


def generate_caption(image: Image.Image) -> dict:

    inputs = processor(image, return_tensors="pt").to(device)

    with torch.no_grad():
        output = model.generate(
            **inputs,
            max_new_tokens=60,
            num_beams=5,
            num_return_sequences=3,
            early_stopping=True,
        )

    captions = list(dict.fromkeys([
        processor.decode(o, skip_special_tokens=True).strip()
        for o in output
    ]))

    # Fallback if all captions are identical
    if len(captions) == 0:
        captions = ["No caption generated."]

    scored = sorted(captions, key=lambda c: len(c.split()), reverse=True)

    return {
        "best_caption": scored[0],
        "candidates": scored,
    }