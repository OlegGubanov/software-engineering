from fastapi.testclient import TestClient
from fastApi import app


client = TestClient(app)


def test_not_found():
    response = client.get('/')
    assert response.status_code == 404


def test_docs():
    response = client.get('/docs')
    assert response.status_code == 200


def test_empty_body():
    response = client.post('/translate')
    assert response.status_code == 422


def test_word():
    response = client.post('/translate', json={'text': 'слово'})
    result = response.json()
    assert response.status_code == 200
    assert result == 'word'


def test_few_words():
    response = client.post('/translate', json={'text': 'пара слов'})
    result = response.json()
    assert response.status_code == 200
    assert result == 'A few words.'


def test_digits():
    response = client.post('/translate', json={'text': '1234567890'})
    result = response.json()
    assert response.status_code == 200
    assert result == '1234567890'
