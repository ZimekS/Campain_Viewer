import os
from app import create_app
from flask import redirect, url_for, request, get_flashed_messages
from flask_login import current_user
from app.model import Campain

def test_add_campain():

    os.environ['FLASK_CONFIG'] = 'testing'
    flask_app = create_app(os.getenv('FLASK_CONFIG') or 'default')

    with flask_app.test_client() as test_client:
        #response = test_client.post('/rejestracja', data=dict(email='zimekpol@gmail.com', name='Filip', password1='password', password2='password'))
        response = test_client.get('/rejestracja')
        assert response.status_code == 200
        assert b"Zapraszamy do rejestracji" in response.data
        
def test_edit_campain_page():

    os.environ['FLASK_CONFIG'] = 'testing'
    flask_app = create_app(os.getenv('FLASK_CONFIG') or 'default')

    with flask_app.test_client() as test_client:
        response = test_client.get('/rejestracja')
        assert response.status_code == 200
        assert b"Zapraszamy do rejestracji" in response.data

def test_add_nonexisting_player():

    os.environ['FLASK_CONFIG'] = 'testing'
    flask_app = create_app(os.getenv('FLASK_CONFIG') or 'default')

    with flask_app.test_client() as test_client:
        response = test_client.get('/rejestracja')
        assert response.status_code == 200
        assert b"Zapraszamy do rejestracji" in response.data
        
def test_add_existing_player():

    os.environ['FLASK_CONFIG'] = 'testing'
    flask_app = create_app(os.getenv('FLASK_CONFIG') or 'default')

    with flask_app.test_client() as test_client:
        response = test_client.get('/rejestracja')
        assert response.status_code == 200
        assert b"Zapraszamy do rejestracji" in response.data
        
def test_edit_campain_info():

    os.environ['FLASK_CONFIG'] = 'testing'
    flask_app = create_app(os.getenv('FLASK_CONFIG') or 'default')

    with flask_app.test_client() as test_client:
        response = test_client.get('/rejestracja')
        assert response.status_code == 200
        assert b"Zapraszamy do rejestracji" in response.data