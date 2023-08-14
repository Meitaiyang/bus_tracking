from flask_sqlalchemy import SQLAlchemy
from celery import Celery, Task

db = SQLAlchemy()
celery = Celery()

# def celery_init_app(app):
#     class FlaskTask(Task):
#         def __call__(self, *args: object, **kwargs: object) -> object:
#             with app.app_context():
#                 return self.run(*args, **kwargs)
# 
#     celery_app = Celery(app.name, task_cls=FlaskTask)
#     celery_app.config_from_object(app.config["CELERY"])
#     celery_app.set_default()
#     app.extensions["celery"] = celery_app
#     return celery_app

def create_test_db(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    db.create_all()