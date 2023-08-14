from flask import jsonify, request
from app.subscribe import bp
from app.extensions import db
from app.subscribe.task import check_users
from app.models.users import Users


@bp.route('/<string: email>/<string: bus_number>/<string: station_name>')
def start_add(email, bus_number, station_name):

    # check if the user is already in the database
    user = Users.query.filter_by(email=email, bus_number).first()
    if user:
        return jsonify({"result_id": "user already exists"})
    result = check_users.delay()
    return jsonify({"result_id": result.id})