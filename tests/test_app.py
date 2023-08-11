import pytest
from app import create_app

@pytest.fixture()
def client():
    App = create_app()
    App.config.update({
        "TESTING": True,
    })

    # other setup can go here

    yield App