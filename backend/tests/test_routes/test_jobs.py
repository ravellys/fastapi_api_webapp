from datetime import datetime
import json


def test_create_job(client):
    data = {
        "title": "teste",
        "company": "teste",
        "company_url": "https://www.teste.com",
        "location": "teste",
        'description': "Test",
    }

    response = client.post("/job/create-job", json.dumps(data))
    assert response.status_code == 200
