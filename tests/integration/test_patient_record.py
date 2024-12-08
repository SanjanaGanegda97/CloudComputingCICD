import requests

BASE_URL = "http://patient-record-service:5000"

def test_create_patient():
    response = requests.post(f"{BASE_URL}/patients", json={
        "id": 1,
        "name": "John Doe",
        "age": 30,
        "medical_history": "None"
    })
    assert response.status_code == 201
    assert "message" in response.json()

def test_get_patient():
    response = requests.get(f"{BASE_URL}/patients/1")
    assert response.status_code == 200
    assert response.json()["id"] == 1
