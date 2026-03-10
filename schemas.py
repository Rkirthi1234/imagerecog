from pydantic import BaseModel
from typing import List, Dict


class CaptionResult(BaseModel):
    best_caption: str
    candidates: List[str]


class CreativeResult(BaseModel):
    style: str
    creative_text: str
    word_count: int


class PredictionResponse(BaseModel):
    caption: CaptionResult
    creative_text: CreativeResult


class AllStylesResponse(BaseModel):
    caption: CaptionResult
    styles: Dict[str, CreativeResult]