from flask import Flask

from config import Config
from app.extensions import db

# need to import the model to create the table
from app.models.buses import Buses
from app.models.stations import Stations
from app.models.bus_station_mapping import BusStationMapping

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize Flask extensions here
    db.init_app(app)

    # Create the table if it doesn't exist
    with app.app_context():
        db.create_all()

    # Register blueprints here
    from app.main import bp as main_bp
    app.register_blueprint(main_bp)

    @app.route('/test/')
    def test_page():
        return '<h1>Testing the Flask Application Factory Pattern</h1>'

    return app
