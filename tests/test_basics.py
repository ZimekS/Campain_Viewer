import pytest
from flask import current_app
from app import create_app

def setUp():
    app = create_app('testing')
    app_context = app.app_context()
    app_context.push()
  
def test_app_exists():
    setUp()
    assert current_app is not None, "App should be running"
    
def test_app_is_testing():
    setUp()
    assert current_app.config['TESTING'] is True, "App should be in testing mode"