import pytest
from app import create_app

@pytest.fixture(scope='module')
def test_app():
    app = create_app()
    app.config.update({
        "TESTING": True,
    })
    with app.app_context():
        yield app

@pytest.fixture(scope='module')
def test_client(test_app):
    testing_client = test_app.test_client()
    yield testing_client
