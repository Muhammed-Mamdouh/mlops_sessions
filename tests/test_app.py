from fastapi.testclient import TestClient

from app import app

client = TestClient(app)


def test_home():
    response = client.get("/home")
    assert response.status_code == 200


def test_predict():
    response = client.post("/predict", json={"a":7, "b":5})
    assert response.status_code == 200
    print(response.content)
