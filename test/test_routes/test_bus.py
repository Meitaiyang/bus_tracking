import json

def test_index_route(test_client):
    
    # test route
    response = test_client.get('/bus/278')
    assert response.status_code == 200

    # test the not found route
    response = test_client.get('/bus/0')
    assert response.status_code == 404
    
    response = test_client.get('/bus/9999')
    assert response.status_code == 404
