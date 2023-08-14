from flask import Flask, jsonify

from config import Config
from celery import Task
from app.extensions import db, celery

# need to import the model to create the table
from app.models.buses import Buses
from app.models.stations import Stations
from app.models.bus_station_mapping import BusStationMapping

from app.data_seeder import insert_simulation_data

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize Flask extensions here
    db.init_app(app)

    app.config.from_mapping(
        CELERY=dict(
            task_ignore_result=True,
        ),
    )
    app.config.from_prefixed_env()
    class FlaskTask(Task):
        def __call__(self, *args: object, **kwargs: object) -> object:
            with app.app_context():
                return self.run(*args, **kwargs)

    celery.config_from_object(app.config["CELERY"])
    celery.set_default()
    app.extensions["celery"] = celery

    # Create the table if it doesn't exist
    with app.app_context():
        db.create_all()
        if not Buses.query.first():
            insert_simulation_data()

    # Register blueprints here
    from app.bus import bp as bus_bp
    app.register_blueprint(bus_bp, url_prefix='/bus')

    from app.subscribe import bp as subscribe_bp
    app.register_blueprint(subscribe_bp, url_prefix='/subscribe')

    @app.route('/test/')
    def test_page():
        return jsonify({'message': 'test message'})
    return app
