import pytest
from flask import current_app, url_for
from app import create_app, db

def test_bp_home_status_code_ok():
    assert current_app != None, 'App should exist'