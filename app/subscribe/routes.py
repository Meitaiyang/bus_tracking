from flask import jsonify, request
from app.subscribe import bp
from app.extensions import db
from app.models.user import Users
from app.subscribe.task import check_users
from app.api import call_api

@bp.route('/<string:email>/<string:bus_number>/<string:direction>/<string:station>')
def subscribe(email, bus_number, direction, station):
    
    # check if the bus, direction and station are valid
    result = call_api(bus_number) 

    if not result:
        return jsonify({"error": "Bus not Found"}), 404   

    for bus in result:
        if bus["direction"] == direction:
            for stop in bus["schedule"]:
                if stop["station_name"] == station:
                    estimated_time = stop["arrival_time"]
                    break
            else:
                return jsonify({"error": "Station not Found"}), 404
            break
        else:
            return jsonify({"error": "Direction not Found"}), 404

    # check if the user is already subscribed
    subscribe_statu = Users.query.filter_by(email=email, bus_number=bus_number, direction=direction, station=station).first()

    if subscribe_statu:
        return jsonify({"error": "User already subscribed"}), 409
    else:
        user = Users(email=email, bus_number=bus_number, direction=direction, station=station, estimated_time=estimated_time)
        db.session.add(user)
        db.session.commit()
        return jsonify({"message": "User subscribed successfully"}), 201
