from app.extensions import db

class BusStationMapping(db.Model):
    mapping_id = db.Column(db.Integer, primary_key=True)
    bus_id = db.Column(db.Integer, db.ForeignKey('buses.bus_id'), nullable=False)
    station_id = db.Column(db.Integer, db.ForeignKey('stations.station_id'), nullable=False)
    arrival_time = db.Column(db.Time, nullable=False)