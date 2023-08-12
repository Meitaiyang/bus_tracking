def test_index_route(test_client):
    response = test_client.get('/bus/1')
    assert response.status_code == 404
