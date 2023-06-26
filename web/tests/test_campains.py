import os
import io
from app import create_app
from flask import redirect, url_for, request, get_flashed_messages
from flask_login import current_user
from app.model import Campain

os.environ['FLASK_CONFIG'] = 'testing'
flask_app = create_app(os.getenv('FLASK_CONFIG') or 'default')

def test_add_campain_page():

    with flask_app.test_client() as test_client:
        #response = test_client.post('/rejestracja', data=dict(email='zimekpol@gmail.com', name='Filip', password1='password', password2='password'))
        #test_client.post('/login', data=dict(email='zimekpol@gmail.com', password='password'))
        response = test_client.get('/dodaj_kampanie')
        assert response.status_code == 200
        assert b"Dodaj kampanie" in response.data
        
def test_add_campain():

    with flask_app.test_client() as test_client:
        test_client.post('/login', data=dict(email='zimekpol@gmail.com', password='password'))
        file = r'/usr/src/campViewer/tests/photo.jpg'
        data = {'name': 'test1', 'description': 'kampania stworzona na potrzeby przeprowadzenia testow', 'file': (open(file, 'rb'), file)}
        test_client.post('/dodaj_kampanie', data=data)
        message = get_flashed_messages(with_categories=True)
        assert message != None
        assert message[1][1] == 'Dodałeś swoją kampanię'
        test_client.post('/login', data=dict(email='zimekpol@gmail.com', password='password'))
        file = r'/usr/src/campViewer/tests/photo2.jpg'
        data = {'name': 'test2', 'description': 'kampania stworzona na potrzeby przeprowadzenia testow', 'file': (open(file, 'rb'), file)}
        test_client.post('/dodaj_kampanie', data=data)

def test_edit_campain_page():

    with flask_app.test_client() as test_client:
        response = test_client.get('/edytuj_kampanie/1')
        assert response.status_code == 200
        assert b"kampania stworzona na potrzeby przeprowadzenia testow" in response.data

def test_add_nonexisting_player():

    with flask_app.test_client() as test_client:
        test_client.post('/login', data=dict(email='zimekpol@gmail.com', password='password'))
        data = {'player': "Romek"}
        test_client.post('/edytuj_kampanie/1', data=data)
        message = get_flashed_messages(with_categories=True)
        assert message[1][1] == 'Nie ma takiego gracza'
        
def test_add_existing_player():

    with flask_app.test_client() as test_client:
        test_client.post('/login', data=dict(email='zimekpol@gmail.com', password='password'))
        data = {'player': "Tytus"}
        test_client.post('/edytuj_kampanie/1', data=data)
        message = get_flashed_messages(with_categories=True)
        assert message[1][1] == 'Dodano gracza Tytus'
        
def test_edit_campain_info():

    with flask_app.test_client() as test_client:
        test_client.post('/login', data=dict(email='zimekpol@gmail.com', password='password'))
        file = r'/usr/src/campViewer/tests/photo.jpg'
        data = {'name': 'test1', 'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.', 'file': (open(file, 'rb'), file)}
        test_client.post('/edytuj_kampanie/1', data=data)
        message = get_flashed_messages(with_categories=True)
        assert message != None
        assert message[1][1] == 'Zaaktualizowano kampanię'