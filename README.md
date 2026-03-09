Here is a **complete `README.md` file** you can directly copy into your GitHub repository.

# Image Caption to Creative Scene Generator

An AI-powered API that converts an uploaded image into a **short caption** and expands it into a **detailed creative scene description** using deep learning models.

This project combines **image captioning (BLIP)** with **text generation (GPT-2)** to transform images into descriptive narratives.

---

## Overview

The system performs two main tasks:

1. **Image Caption Generation**

   * Uses the **BLIP Image Captioning model** to analyze an uploaded image.
   * Produces a short descriptive caption.

2. **Creative Scene Generation**

   * Uses **GPT-2** to expand the caption.
   * Generates a **detailed ~250 word scene description**.

The project is implemented as a **FastAPI service**, allowing users to upload images and receive generated descriptions through an API endpoint.

---

## Features

* Image upload API
* Automatic caption generation
* AI-generated creative scene descriptions
* FastAPI based REST service
* Uses HuggingFace Transformers models

---

## Tech Stack

* Python
* FastAPI
* HuggingFace Transformers
* BLIP Image Captioning Model
* GPT-2 Text Generation Model
* Pydantic
* Uvicorn

---

## Project Structure

```
imagerecognition/
│
├── app/
│   ├── main.py          # FastAPI application
│   ├── model.py         # BLIP image caption generation
│   ├── generator.py     # GPT-2 creative text generator
│   ├── schemas.py       # Response schema
│   └── utils.py         # Image loading utilities
│
├── requirements.txt
└── README.md
```

---

## Installation

Clone the repository

```
git clone https://github.com/your-username/image-caption-generator.git
cd image-caption-generator
```

Create a virtual environment

```
python -m venv .venv
```

Activate the virtual environment

Windows

```
.venv\Scripts\activate
```

Install dependencies

```
pip install -r requirements.txt
```

---

## Running the Application

Start the FastAPI server:

```
python -m uvicorn app.main:app --reload
```

The API will run at:

```
http://127.0.0.1:8000
```

---

## API Documentation

FastAPI automatically provides interactive documentation.

Swagger UI:

```
http://127.0.0.1:8000/docs
```

---

## API Endpoint

### POST `/predict`

Upload an image to generate a caption and creative description.

#### Request

Form Data

```
file: image
```

#### Example Response

```json
{
  "caption": "a dog running through a grassy field",
  "creative_text": "The golden retriever dashed across the open meadow, its golden fur catching the sunlight as it bounded through the tall grass..."
}
```

---

## Workflow

1. User uploads an image.
2. The BLIP model generates a caption.
3. The caption is sent to the GPT-2 generator.
4. GPT-2 produces a detailed creative description.

---
