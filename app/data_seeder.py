from datetime import datetime
from app.models.buses import Buses
from app.models.stations import Stations
from app.models.bus_station_mapping import BusStationMapping
from app.extensions import db
import json


def insert_simulation_data():

    with open('app/static/bus.json') as f:
        simulation_data = json.load(f)


    for bus_data in simulation_data:
        # Create or fetch the Bus
        bus = Buses.query.filter_by(bus_number=bus_data['bus_number']).first()
        if not bus:
            bus = Buses(bus_number=bus_data['bus_number'], direction=bus_data['direction'])
            db.session.add(bus)
            db.session.commit()

        for schedule in bus_data['schedule']:
            # Create or fetch the Station
            station = Stations.query.filter_by(station_name=schedule['station_name']).first()
            if not station:
                station = Stations(station_name=schedule['station_name'])
                db.session.add(station)
                db.session.commit()

            # Convert the string arrival time to a Time object
            time_obj = datetime.strptime(schedule['arrival_time'], "%H:%M").time()
            
            # Create the BusStationMapping
            mapping = BusStationMapping(bus_id=bus.bus_id, station_id=station.station_id, arrival_time=time_obj)
            db.session.add(mapping)

    db.session.commit()
