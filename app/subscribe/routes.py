from flask import jsonify, request
from app.subscribe import bp
from app.extensions import db
from app.subscribe.task import check_users


@bp.route('/add')
def start_add():
    result = check_users.delay()
    return jsonify({"result_id": result.id})