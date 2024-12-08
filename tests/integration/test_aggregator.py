import requests

BASE_URL = "http://aggregator-service:5003"

def test_aggregate_data():
    response = requests.get(f"{BASE_URL}/aggregate")
    assert response.status_code == 200
    assert "aggregated_data" in response.json()
