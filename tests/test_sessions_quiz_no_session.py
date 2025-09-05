import pytest
from Python.web.Sessions.quiz_no_session import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_index(client):
    response = client.get('/')
    assert "Тест" in response.data.decode()

def test_result(client):
    response = client.get('/result')
    assert "that's all folks!" in response.data.decode()