import json
import pytest
from app import create_app

# Fixture to create an instance of the Flask app
@pytest.fixture()
def client():
    App = create_app()
    App.config.update({
        "TESTING": True,
    })
    
    with App.test_client() as client:
        yield client

# Test function that uses the 'client' fixture
def test_json_data(client):
    response = client.get('/test/')
    res = json.loads(response.data.decode('utf-8')).get("message")
    assert res == "test message"

def test_bus(client):
    response = client.get('/bus/1/')
    print(response.json())
    """
    if response.status_code == 404:
        res = json.loads(response.data.decode('utf-8')).get("error")
        assert response.json()["error"] == "Bus not found"
    else:
        res = json.loads(response.data.decode('utf-8')).get("message")
        assert res == "Hello, World!"
    """