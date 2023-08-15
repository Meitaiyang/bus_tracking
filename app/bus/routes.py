from flask import jsonify
from app.bus import bp
from app.extensions import db
from app.api import call_api

@bp.route('/<string:bus_number>')
def index(bus_number):
    
    result = call_api(bus_number) 

    if not result:
        return jsonify({"error": "Bus not Found"}), 404   

    return jsonify(result), 200