import requests

BASE_URL = "http://appointment-scheduling-service:5001"

def test_create_appointment():
    response = requests.post(f"{BASE_URL}/appointments", json={
        "id": 1,
        "patient_id": 1,
        "doctor_id": 101,
        "time": "2024-12-05T10:00:00",
        "notes": "Initial consultation"
    })
    assert response.status_code == 201
    assert "message" in response.json()

def test_get_appointments_by_doctor():
    response = requests.get(f"{BASE_URL}/appointments/doctor/101")
    assert response.status_code == 200
    assert len(response.json()) > 0
