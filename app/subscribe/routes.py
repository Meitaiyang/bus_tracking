from flask import jsonify, request
from app.subscribe import bp
from app.extensions import db
from app.subscribe.task import add_together


@bp.route('/add')
def start_add():
    a = request.form.get("a", type=int)
    b = request.form.get("b", type=int)
    result = add_together.delay(a, b)
    return {"result_id": result.id}