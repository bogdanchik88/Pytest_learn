def test_client(client):
    responce = client.get('/api')

    assert responce.status_code == 200