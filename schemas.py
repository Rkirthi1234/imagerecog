from pydantic import BaseModel


class PredictionResponse(BaseModel):
    caption: str
    creative_text: str