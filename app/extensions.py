from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

def create_test_db(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    db.create_all()