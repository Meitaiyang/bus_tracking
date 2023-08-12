def test_index_route(test_client):
    
    # test the not found route
    response_fail = test_client.get('/bus/1')
    assert response_fail.status_code == 404

    # test the exist route 278
    response_success = test_client.get('/bus/278')
    assert response_success.status_code == 200
