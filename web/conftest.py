import pytest
import os

from app import create_app

@pytest.fixture
def app():
    app = create_app(os.getenv('FLASK_CONFIG') or 'default')
    app.app_context().push()
    return app
