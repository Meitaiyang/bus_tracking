from app.extensions import db

class Buses(db.Model):
    bus_id = db.Column(db.Integer, primary_key=True)
    bus_number = db.Column(db.String, nullable=False)
    direction = db.Column(db.String, nullable=False)
    mappings = db.relationship('BusStationMapping', backref='bus', lazy=True)