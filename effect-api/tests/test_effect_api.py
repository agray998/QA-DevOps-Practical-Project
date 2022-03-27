from fastapi.testclient import TestClient
# import the app's classes and objects
from application import app

client = TestClient(app)

def test_get_effect():
    response = client.post('/get_effect', json={"event": "Weapons Upgrade", "unit": "Ranged inf."})
    assert response.status_code == 200
    assert response.text == '+10 to Range'