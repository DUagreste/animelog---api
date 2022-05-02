from pydantic import BaseModel, validator
from datetime import datetime
from fastapi import HTTPException, status


class AnimeOut(BaseModel):
    id: int
    name: str
    studios: str
    genres: str
    episodes: int
    score: float
    date: datetime


class AnimeIn(BaseModel):
    name: str
    studios: str
    genres: str
    episodes: int
    score: float

    @validator("score")
    def validate_score(cls, v, field):
        if v <= 1 or v > 10:
            raise HTTPException(
                detail=f"{field.name} must be between 0 and 10",
                status_code=status.HTTP_400_BAD_REQUEST
            )
        return v
