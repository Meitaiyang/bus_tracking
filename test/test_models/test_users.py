from app.models.user import Users
from app.api import call_api

# testing the Buses model with bus_number = 278
def test_get_all_buses(test_client):
    response = test_client.get('/bus/278')
    bus = Buses.query.filter_by(bus_number='278').first()
    assert bus.bus_number == '278'
    assert bus.direction == '捷運景美'
