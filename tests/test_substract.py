import pytest

@pytest.mark.parametrize(
        'a, b, res, status_code',
        [
            (5, 2, 3, 200),
            (4, 9, -5, 200),
            (0, 0, 0, 200),
            (-4, 6, -10, 200),
            (7, -2, 9, 200),
            (-8, -9, 1, 200),
            ('1', 5, -4, 200),
            (3, '-8', 11, 200),
            ('-4', '2', -6, 200),
            ('darov', [1, 2, 3], None, 422),
        ]
)
def test_substract(client, a, b, res, status_code):
    responce = client.get('/api/substract', params= {'a': a, 'b': b})

    assert responce.status_code == status_code
    if res:
        assert responce.json()['result'] == res