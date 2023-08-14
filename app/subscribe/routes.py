from flask import jsonify
from app.subscribe import bp
from app.extensions import db

@bp.route('/<string:bus_number>')
def index(bus_number):
    return jsonify({'message': 'bus not found'}), 404
