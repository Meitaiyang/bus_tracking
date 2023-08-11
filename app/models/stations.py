from app.extensions import db

class Stations(db.Model):
    station_id = db.Column(db.Integer, primary_key=True)
    station_name = db.Column(db.String, nullable=False)
    mappings = db.relationship('BusStationMapping', backref='station', lazy=True)