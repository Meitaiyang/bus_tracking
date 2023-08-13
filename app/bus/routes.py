from flask import jsonify
from app.bus import bp
from app.extensions import db
from app.models.buses import Buses
from app.models.stations import Stations
from app.models.bus_station_mapping import BusStationMapping

@bp.route('/<string:bus_number>')
def index(bus_number):
    
    # search the bus number in the database
    bus = Buses.query.filter_by(bus_number=str(bus_number)).first()

    if not bus:
        return jsonify({'message': 'bus not found'}), 404

    # get the bus station mapping
    bus_station_mapping = BusStationMapping.query.filter_by(bus_id=bus.bus_id).all()

    # get the station name from the station id
    for mapping in bus_station_mapping:
        station = Stations.query.filter_by(station_id=mapping.station_id).first()
        mapping.station_name = station.station_name
    

    return jsonify({
        'bus_number': bus_number, 
        'direction':bus.direction,
        'schedule': 
        [
            {'station_name':mapping.station_name, 
            'arrival_time':mapping.arrival_time.strftime('%H:%M')} 
            for mapping in bus_station_mapping
        ]
        }), 200