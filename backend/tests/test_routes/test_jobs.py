from datetime import datetime
import json


def test_create_job(client):
    data = {
        "title": "teste",
        "company": "teste",
        "company_url": "https://www.teste.com",
        "location": "teste",
        'description': "Test",
        'date_posted': "2021-01-01",
    }

    response = client.post("/job/create-job", json.dumps(data))
    assert response.status_code == 200


def test_retreive_job_by_id(client):
    data = {
        "title": "teste",
        "company": "teste",
        "company_url": "https://www.teste.com",
        "location": "teste",
        'description': "Test",
        'date_posted': "2021-01-01",
    }

    client.post("v1/jobs/", json.dumps(data))
    response = client.get("v1/jobs/1")
    assert response.status_code == 200
    assert response.json()["title"] == data["title"]