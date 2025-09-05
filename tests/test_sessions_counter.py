import pytest
from Python.web.Sessions.Counter import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_counter(client):
    response = client.get('/')
    assert "Счётчик" in response.data.decode()