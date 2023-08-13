from app.extensions import db

class Users(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    mappings = db.relationship('BusStationMapping', backref='bus', lazy=True)