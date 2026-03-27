import pytest

@pytest.mark.parametrize(
        'a, b, res, status_code',
        [
            (1, 2, 3, 200),
            (4, 5, 9, 200),
            (0, 0, 0, 200),
            (-4, -9, -13, 200),
            (-3, 8, 5, 200),
            (9, -7, 2, 200),
            (0, 'hello', None, 422),
            (True, [1, 2, 3], None, 422),
            ({'num1': 1, 'num2': 4}, (1, 5), None, 422),
        ]
)
def test_append(a, b, res, status_code, client):
    responce = client.get('/api/append', params={'a': a, 'b': b})

    assert responce.status_code == status_code
    if res:
        assert responce.json()['result'] == res