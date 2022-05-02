import typer
from typing import Optional
from core import add_anime_to_database, get_animes_from_database
from rich.table import Table
from rich.console import Console
from rich import print

main = typer.Typer(help="Anime Management Application")

console = Console()


@main.command()
def add(
    name: str,
    studios: str,
    genres: str = typer.Option(...),
    episodes: int = typer.Option(...),
    score: float = typer.Option(...)
):
    """Adds a new anime to the database"""
    if add_anime_to_database(name, studios, genres, episodes, score):
        print("👾 Anime added to database! 🤖")
    else:
        print("👹 Error - cannot add anime. 💀")


@main.command("list")
def list_animes(name: Optional[str] = None):
    """Lists beers from the database"""
    animes = get_animes_from_database(name)
    table = Table(
        title="Animelog Database 🐲" if not name else f"Animelog {name}"
    )
    headers = [
        "id",
        "name",
        "studios",
        "genres",
        "episodes",
        "score",
        "date"
    ]
    for header in headers:
        table.add_column(header, style="red")
    for anime in animes:
        anime.date = anime.date.strftime("%Y-%m-%d")
        values = [str(getattr(anime, header)) for header in headers]
        table.add_row(*values)
    console.print(table)


if __name__ == "__main__":
    main()
