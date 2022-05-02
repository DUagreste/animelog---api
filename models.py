from typing import Optional
from sqlmodel import SQLModel, Field
from pydantic import validator
from datetime import datetime


class Anime(SQLModel, table=True):
    __table_args__ = {'extend_existing': True}
    id: Optional[int] = Field(primary_key=True, default=None, index=True)
    name: str
    studios: str
    genres: str
    episodes: int
    score: float
    date: datetime = Field(default_factory=datetime.now)

    @validator("score")
    def validate_score(cls, v, field):
        if v <= 1 or v > 10:
            raise RuntimeError(f"{field.name} must be between 0 and 10.")
        return v
