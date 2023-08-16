from app.extensions import db

class Users(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), nullable=False)
    bus_number = db.Column(db.Integer, nullable=False)
    direction = db.Column(db.String(120), nullable=False)
    station = db.Column(db.String(120), nullable=False)
    estimated_time = db.Column(db.Integer, nullable=False)
