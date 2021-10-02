import json


def test_create_user(client):
    data = {
        "username": "teste_username",
        "email": "teste@email.com",
        "password": "teste"
    }
    response = client.post("v1/users/", json.dumps(data))
    assert response.status_code == 200
    assert response.json()["email"] == data["email"]
    assert response.json()["is_active"] == True
