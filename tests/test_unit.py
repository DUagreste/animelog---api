from animelog.core import get_animes_from_database, add_anime_to_database


def test_add_anime_to_database():
    assert add_anime_to_database("Cowboy Bebop", "Sunrise", "sci-fi, action",
                                 26, 8.7)


def test_get_animes_from_database():
    results = get_animes_from_database()
    assert len(results) > 0
