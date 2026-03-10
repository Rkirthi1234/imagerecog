import re
import os
from groq import Groq
from dotenv import load_dotenv
from pathlib import Path

load_dotenv(dotenv_path=Path(__file__).resolve().parent.parent / ".env")

api_key = os.getenv("GROQ_API_KEY")
if not api_key:
    raise ValueError("GROQ_API_KEY environment variable is not set.")

client = Groq(api_key=api_key)

STYLES = {
    "vivid": "Write a vivid, sensory-rich scene description of 150-200 words.",
    "Artistic": "Write a poetic and lyrical scene description of 150-200 words.",
    "cinematic": "Write a cinematic, movie-scene-like description of 150-200 words.",
    "playful": "Write a fun, simple story for children of 150-200 words.",
}


def generate_creative_text(caption: str, style: str = "vivid") -> dict:

    style_instruction = STYLES.get(style, STYLES["vivid"])

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "system",
                "content": (
                    "You are a creative writing assistant. "
                    "Stay strictly on the given caption topic. "
                    "Output only the scene description, nothing else."
                ),
            },
            {
                "role": "user",
                "content": f"{style_instruction}\n\nCaption: {caption}",
            },
        ],
        temperature=0.8,
        top_p=0.9,
        frequency_penalty=0.3,
        presence_penalty=0.2,
        max_tokens=400,
    )

    text = response.choices[0].message.content.strip()
    word_count = len(re.findall(r"\w+", text))

    return {
        "style": style,
        "creative_text": text,
        "word_count": word_count,
    }


def generate_all_styles(caption: str) -> dict:
    results = {}
    for style in STYLES:
        results[style] = generate_creative_text(caption, style)
    return results