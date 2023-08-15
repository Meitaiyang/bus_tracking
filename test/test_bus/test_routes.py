import json

def test_index_route(test_client):
    
    # test the not found route
    response_fail = test_client.get('/bus/1')
    assert response_fail.status_code == 404

    # test the exist route 278
    # read the json file first

    with open('app/static/bus.json') as f:
        simulation_data = json.load(f)
        test_bus_number = '278'

        test_dict = None
        for item in simulation_data:
            if item["bus_number"] == test_bus_number:
                test_dict = item
                break

    response_success = test_client.get('/bus/672')
    assert response_success.status_code == 200

    # test the response data json
    assert response_success.json == test_dict
