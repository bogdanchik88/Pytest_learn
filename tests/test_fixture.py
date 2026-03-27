def test_client(client):
    responce = client.get('/docs')

    assert responce.status_code == 200