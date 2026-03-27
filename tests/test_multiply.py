import pytest

@pytest.mark.parametrize(
        'a, b, res, status_code',
        [
            (2, 3, 6, 200),
            (7, 0.5, 3.5, 200),
            (5, -6, -30, 200),
            (-3, -14, 42, 200),
            ('str', 67, None, 422),
            ('1 st', '2 st', None, 422),
            ([1, 2, 3], (4, 5), None, 200),
        ]
)
def test_multiply(client, a, b, res, status_code):
    responce = client.get('/api/multiply', params={'a': a, 'b': b})

    assert responce.status_code == status_code
    if res:
        assert responce.json()['result'] == res