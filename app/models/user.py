from app.extensions import db

class Users(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    bus_id = db.Column(db.Integer, db.ForeignKey('bus.bus_id'), nullable=False)
    station_id = db.Column(db.Integer, db.ForeignKey('bus_station.station_id'), nullable=False)
    mappings = db.relationship('BusStationMapping', backref='bus', lazy=True)