from flask_sqlalchemy import SQLAlchemy
from celery import Celery, Task
from flask_mail import Mail

db = SQLAlchemy()
celery = Celery()
mail = Mail()

def create_test_db(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    db.create_all()