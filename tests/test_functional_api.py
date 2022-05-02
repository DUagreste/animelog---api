from fastapi.testclient import TestClient

from api import api

client = TestClient(api)


def test_create_anime_via_api():
    response = client.post(
        "/animes/",
        json={
            "name": "Dragon Ball Z",
            "studios": "Toei",
            "genres": "action, comedy, adventure",
            "episodes": 291,
            "score": 8.1,
        }
    )
    assert response.status_code == 200
    result = response.json()
    assert result["name"] == "Dragon Ball Z"
