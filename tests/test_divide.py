import pytest

@pytest.mark.parametrize(
        'a, b, res, div_integer, status_code',
        [
            (2, 4, 0.5, False, 200),
            (6, 0, None, False, 400),
            (5, 7, 0, True, 200),
            (16, 5, 3, True, 200)
        ]
)
def test_divide(client, a, b, res, div_integer, status_code):
    responce = client.get('/api/divide', params={'a': a, 'b': b, 'div_integer': div_integer})

    assert responce.status_code == status_code
    if res is not None:
        assert responce.json()['result'] == res