import requests

BASE = "https://jsonplaceholder.typicode.com"

def test_get_post():
    response = requests.get(BASE + "/posts/1")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == 1
    assert data["title"] != ""


def test_post_not_found():
    response = requests.get(BASE + "/posts/99999")
    assert response.status_code == 404

def test_create_post():
    new = {
        "title": "Светильник из хлеба",
        "body": "Хлеб, который не съели",
        "userId": 1,
    }
    response = requests.post(BASE + "/posts", json=new)
    assert response.status_code == 201
    data = response.json()
    assert data["title"] == new["title"]
    assert "id" in data