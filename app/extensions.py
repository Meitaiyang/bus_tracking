from flask_sqlalchemy import SQLAlchemy
from celery import Celery

db = SQLAlchemy()
celery = Celery()

def create_test_db(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    db.create_all()