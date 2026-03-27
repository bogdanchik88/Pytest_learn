import pytest

def test_func():
    assert 2 == 2

@pytest.mark.parametrize(
        'a, b, res',
        [
            (1, 2, 3),
            (4, 5, 9),
            (0, 0, 0),
        ]
)
def test_append(a, b, res, client):
    responce = client.get(f'/api/append?a={a}&b={b}')

    assert responce.status_code == 200
    assert responce.json()['result'] == res

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