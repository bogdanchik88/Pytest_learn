import pytest

@pytest.mark.parametrize(
        'a, b, res, status_code',
        [
            (5, 2, 3, 200),
        ]
)
def test_substract(client, a, b, res, status_code):
    responce = client.get('/api/substract', params= {'a': a, 'b': b})

    assert responce.status_code == status_code
    assert responce.json()['result'] == res