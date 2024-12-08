import requests

BASE_URL = "http://notification-service:5002"

def test_send_notification():
    response = requests.post(f"{BASE_URL}/notifications", json={
        "id": 1,
        "recipient_email": "user@example.com",
        "subject": "Appointment Reminder",
        "message": "Your appointment is scheduled for 2024-12-05."
    })
    assert response.status_code == 200
    assert "message" in response.json()
