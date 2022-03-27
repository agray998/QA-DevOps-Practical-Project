from fastapi.testclient import TestClient
from unittest.mock import patch
# import the app's classes and objects
from application import app

client = TestClient(app)

@patch('random.choice', return_value = "Ranged inf.")
def test_get_name():
    response = client.get('/get_unit')
    assert response.status_code == 200
    assert response.text == 'Ranged inf.'