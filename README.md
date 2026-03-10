# Image Recognition API

A FastAPI-based image recognition API that generates detailed creative descriptions from uploaded images. It uses **BLIP-large** for image captioning and **LLaMA 3.3 70B (via Groq)** for creative text generation in multiple styles.

---

## Tech Stack

| Component | Technology |
|---|---|
| API Framework | FastAPI |
| Image Captioning | Salesforce BLIP-large |
| Creative Text | LLaMA 3.3 70B (Groq API) |
| Image Processing | Pillow |
| ML Framework | PyTorch + HuggingFace Transformers |

---

## Project Structure

```
imagerecognition/
├── app/
│   ├── generator.py     # Creative text generation (Groq + LLaMA)
│   ├── main.py          # FastAPI routes and endpoints
│   ├── model.py         # Image captioning (BLIP-large)
│   ├── schemas.py       # Pydantic response models
│   └── utils.py         # Image preprocessing
├── .env                 # API keys (never commit this)
└── requirements.txt
```

---

## Required API Keys

Add these to your `.env` file in the project root:

```env
GROQ_API_KEY=gsk_xxxxxxxxxxxx
HF_TOKEN=hf_xxxxxxxxxxxx
```

| Key | Required | Get it from |
|---|---|---|
| `GROQ_API_KEY` | Yes | https://console.groq.com → API Keys (Free) |
| `HF_TOKEN` | Optional | https://huggingface.co/settings/tokens (Free) |

---

## Installation

```bash
# Create and activate virtual environment
python -m venv .venv
.venv\Scripts\activate        # Windows
source .venv/bin/activate     # Mac/Linux

# Install dependencies
pip install fastapi uvicorn transformers torch pillow groq python-dotenv
```

---

## Run the API

```bash
python -m uvicorn app.main:app --reload
```

Server starts at: **http://127.0.0.1:8000**
Swagger UI at: **http://127.0.0.1:8000/docs**

---

## Endpoints

### `POST /predict`
Upload an image and get a caption + creative description in a chosen style.

**Query Parameter:**
- `style` — `vivid` | `artistic` | `cinematic` | `playful` (default: `vivid`)

**Example Response:**
```json
{
  "caption": {
    "best_caption": "a dog running in a green field",
    "candidates": [
      "a dog running in a green field",
      "a brown dog playing in a field"
    ]
  },
  "creative_text": {
    "style": "vivid",
    "creative_text": "The golden retriever bursts across the emerald field...",
    "word_count": 172
  }
}
```

---

### `POST /predict/all-styles`
Upload an image and get creative descriptions in **all 4 styles** at once.

**Example Response:**
```json
{
  "caption": { "best_caption": "...", "candidates": [] },
  "styles": {
    "vivid": { "style": "vivid", "creative_text": "...", "word_count": 165 },
    "artistic": { "style": "artistic", "creative_text": "...", "word_count": 170 },
    "cinematic": { "style": "cinematic", "creative_text": "...", "word_count": 168 },
    "playful": { "style": "playful", "creative_text": "...", "word_count": 160 }
  }
}
```

---

### `GET /styles`
Returns a list of all available styles.

```json
{
  "styles": ["vivid", "artistic", "cinematic", "playful"],
  "default": "vivid"
}
```

---

## Writing Styles

| Style | Description |
|---|---|
| **vivid** | Sensory-rich scene with colors, textures, sounds and smells |
| **artistic** | Expressive and visually imaginative like a painting description |
| **cinematic** | Dramatic movie-scene style with lighting and atmosphere |
| **playful** | Fun, simple and childish tone that kids will enjoy |

---

## How It Works

```
1. Image uploaded via API
2. utils.py   → Resize to max 1024px + sharpen for better accuracy
3. model.py   → BLIP-large generates 3 caption candidates using Beam Search
               → Picks the most detailed caption
4. generator.py → Sends caption to Groq (LLaMA 3.3 70B)
                → Returns 150-200 word creative description in chosen style
5. main.py    → Caches result in memory to avoid duplicate API calls
               → Returns JSON response
```

---

## Performance Notes

- BLIP-large model (~1.88GB) downloads **once** and is cached locally at `~/.cache/huggingface`
- In-memory caching means repeated requests for the same image+style are **instant**
- Groq API responds in **under 1 second** (runs on their servers, no local GPU needed)
- Runs on **CPU** by default — GPU is used automatically if available
