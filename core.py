from typing import List, Optional
from sqlmodel import select
from database import get_session
from models import Anime


def add_anime_to_database(
    name: str,
    studios: str,
    genres: str,
    episodes: int,
    score: float
) -> bool:
    with get_session() as session:
        anime = Anime(**locals())
        session.add(anime)
        session.commit()

    return True


def get_animes_from_database(name: Optional[str] = None) -> List[Anime]:
    with get_session() as session:
        sql = select(Anime)
        if name:
            sql = sql.where(Anime.name == name)
        return list(session.exec(sql))
