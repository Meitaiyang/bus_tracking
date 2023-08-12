from flask import jsonify
from app.main import bp
from app.extensions import db
from app.models.bus_station_mapping import BusStationMapping

@bp.route('/bus/<bus_number>')
def index(bus_number):
    
    # search the bus and arrive time in BusStationMapping table
    bus_station_mapping = BusStationMapping.query.filter_by(bus_number=bus_number).all()
    if not bus_station_mapping:
        return jsonify({'message': 'bus not found'}), 404
    return jsonify({'bus_number': bus_number, 'arrive_time': [mapping.arrival_time for mapping in bus_station_mapping]}), 200