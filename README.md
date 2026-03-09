# imagerecog
This project is an AI-powered Image Recognition API that generates a caption from an uploaded image and expands it into a detailed creative scene description using deep learning models.

Project Structure
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
Installation

Clone the repository

git clone https://github.com/your-username/image-caption-generator.git
cd image-caption-generator

Create a virtual environment

python -m venv .venv

Activate the virtual environment

Windows

.venv\Scripts\activate

Install dependencies

pip install -r requirements.txt
Running the Application

Start the FastAPI server:

python -m uvicorn app.main:app --reload

The API will run at:

http://127.0.0.1:8000
API Documentation

FastAPI automatically provides interactive documentation.

Swagger UI:

http://127.0.0.1:8000/docs
API Endpoint
POST /predict

Upload an image to generate a caption and creative description.

Request

Form Data

file: image
Example Response
{
  "caption": "a dog running through a grassy field",
  "creative_text": "The golden retriever dashed across the open meadow, its golden fur catching the sunlight as it bounded through the tall grass..."
}
