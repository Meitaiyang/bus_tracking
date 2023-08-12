from datetime import datetime
from app.models.buses import Buses
from app.models.stations import Stations
from app.models.bus_station_mapping import BusStationMapping
from app.extensions import db

simulation_data = [
    {
        "bus_number": 672,
        "direction": "往大鵬新城",
        "schedule": [
            {"station_name": "健康新城", "arrival_time": "12:00"},
            {"station_name": "博仁醫院", "arrival_time": "12:20"},
            {"station_name": "市民住宅", "arrival_time": "12:40"},
            {"station_name": "喬治商職", "arrival_time": "13:00"},
            {"station_name": "臺大癌醫", "arrival_time": "13:20"},
            {"station_name": "永元路", "arrival_time": "13:40"},
            {"station_name": "中興二村", "arrival_time": "14:00"}
        ]
    },
    {
        "bus_number": 278,
        "direction": "捷運景美",
        "schedule": [
            {"station_name": "內湖國小", "arrival_time": "9:00"},
            {"station_name": "捷運文德站(碧湖公園)", "arrival_time": "9:20"},
            {"station_name": "三總內湖站", "arrival_time": "9:40"},
            {"station_name": "時報廣場", "arrival_time": "10:00"},
            {"station_name": "新東街口", "arrival_time": "10:20"},
            {"station_name": "長壽公園", "arrival_time": "10:40"},
            {"station_name": "博仁醫院", "arrival_time": "11:00"},
            {"station_name": "阿波羅大廈", "arrival_time": "11:20"}
        ]
    }
]

def insert_simulation_data(simulation_data):
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
