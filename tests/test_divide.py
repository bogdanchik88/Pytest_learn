import pytest

def test_divide(client):
    responce = client.get('/api/divide', params={'a': 7, 'b': 2, 'div_integer': True})

    assert responce.status_code == 200
    assert responce.json()['result'] == 3