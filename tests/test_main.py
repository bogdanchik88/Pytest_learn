import pytest

def test_func():
    assert 2 == 2

def test_substract(client):
    responce = client.get('/api/substract?a=8&b=3')

    assert responce.status_code == 200
    assert responce.json()['result'] == 5

def test_multiply(client):
    responce = client.get('api/multiply?a=4&b=3')

    assert responce.status_code == 200
    assert responce.json()['result'] == 12

def test_divide(client):
    responce = client.get('api/divide?a=10&b=4')

    assert responce.status_code == 200
    assert responce.json()['result'] == 2.5