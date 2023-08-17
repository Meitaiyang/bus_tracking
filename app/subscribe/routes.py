import re
from datetime import datetime
from flask import jsonify, request
from flask_mail import Message
from app.subscribe import bp
from app.extensions import db, mail
from app.models.user import Users
from app.api import call_api

EMAIL_REGEX = re.compile(r"[^@]+@[^@]+\.[^@]+")

@bp.route('/<string:email>/<string:bus_number>/<string:direction>/<string:station>')
def subscribe(email, bus_number, direction, station):

    # check if the email is valid
    if not EMAIL_REGEX.match(email):
        return jsonify({"error": "Invalid Email"}), 400
    
    # check if the bus, direction and station are valid
    result = call_api(bus_number) 

    # if the bus is not found
    if not result:
        return jsonify({"error": "Bus not Found"}), 404   

    for bus in result:

        if bus["direction"] == direction:
            for stop in bus["schedule"]:
                if stop["station_name"] == station:
                    estimated_time = stop["arrival_time"] + int(datetime.now().timestamp())
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

@bp.route('/<string:user>')
def query_user(user):
    # find all user with no condition
    user_info = list()
    for u in Users.query.all():
        user_info.append(
            {"user_id": u.user_id,
            "email": u.email,
            "bus_number": u.bus_number,
            "direction": u.direction,
            "station": u.station,
            "estimated_time": u.estimated_time
            }
        )


    return jsonify(user_info), 200

@bp.route('/delete/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = Users.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    return jsonify({"message": "User deleted successfully"}), 200

@bp.route('/mail/<int:user_id>', methods=['POST'])
def send_mail(user_id):
    # create a new email message

    user = Users.query.get_or_404(user_id)
    msg = Message('Bus Arrival Alert', sender='gmail.com', recipients=[user.email])
    msg.body = f"The bus number {user['bus_number']} is arriving at station {user.station} in less than 3 minutes."

    # send the email
    mail.send(msg)
