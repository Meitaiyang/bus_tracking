from flask import Blueprint

bp = Blueprint('bus', __name__)

from app.bus import routes