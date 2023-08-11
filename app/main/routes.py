from flask import jsonify
from app.main import bp
from app.extensions import db


@bp.route('/')
def index():
    return jsonify({'message': 'Hello, World!'})