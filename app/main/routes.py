from flask import jsonify
from app.main import bp
from app.extensions import db
from app.models.buses import Buses


@bp.route('/bus/<bus_number>')
def index(bus_number):
    bus = Buses.query.filter_by(bus_number=bus_number).first()
    if not bus:
        return jsonify({"error": "Bus not found"}), 404
    return jsonify({'message': 'Hello, World!'})