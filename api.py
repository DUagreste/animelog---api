from typing import List
from fastapi import FastAPI
from core import get_animes_from_database
from serializers import AnimeIn, AnimeOut
from models import Anime
from database import get_session

api = FastAPI(title="Animelog")


@api.get("/animes/", response_model=List[AnimeOut])
async def list_animes():
    animes = get_animes_from_database()
    return animes


@api.post("/animes/", response_model=AnimeOut)
async def add_anime(anime_in: AnimeIn):
    anime = Anime(**anime_in.dict())
    with get_session() as session:
        session.add(anime)
        session.commit()
        session.refresh(anime)
    return anime
