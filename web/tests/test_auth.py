import os
from app import create_app
from flask import redirect, url_for, request, get_flashed_messages
from app.model import User


def test_signup_page():
    """
    GIVEN a Flask application configured for testing
    WHEN the '/' page is requested (GET)
    THEN check that the response is valid
    """
    # Set the Testing configuration prior to creating the Flask application
    os.environ['FLASK_CONFIG'] = 'testing'
    flask_app = create_app(os.getenv('FLASK_CONFIG') or 'default')

    # Create a test client using the Flask application configured for testing
    with flask_app.test_client() as test_client:
        response = test_client.get('/rejestracja')
        assert response.status_code == 200
        assert b"Zapraszamy do rejestracji" in response.data
        
def test_login_page():
    """
    GIVEN a Flask application configured for testing
    WHEN the '/' page is requested (GET)
    THEN check that the response is valid
    """
    # Set the Testing configuration prior to creating the Flask application
    os.environ['FLASK_CONFIG'] = 'testing'
    flask_app = create_app(os.getenv('FLASK_CONFIG') or 'default')

    # Create a test client using the Flask application configured for testing
    with flask_app.test_client() as test_client:
        response = test_client.get('/login')
        assert response.status_code == 200
        assert b"Logowanie" in response.data
        
def test_logout_page():
    """
    GIVEN a Flask application configured for testing
    WHEN the '/' page is requested (GET)
    THEN check that the response is valid
    """
    # Set the Testing configuration prior to creating the Flask application
    os.environ['FLASK_CONFIG'] = 'testing'
    flask_app = create_app(os.getenv('FLASK_CONFIG') or 'default')
    client = flask_app.test_client()
    
    with flask_app.test_client() as test_client:
        
        response = test_client.get('/wylogowanie', follow_redirects=True)
        message = get_flashed_messages(with_categories=True)
        assert response.status_code == 200
        assert message != None
        assert message[0][1] == 'Please log in to access this page.'
    
def test_too_short_name():
    os.environ['FLASK_CONFIG'] = 'testing'
    flask_app = create_app(os.getenv('FLASK_CONFIG') or 'default')

    with flask_app.test_client() as test_client:
        response = test_client.post('/rejestracja', data=dict(email='test@test.com', name='Va', password1='password', password2='password'))
        message = get_flashed_messages(with_categories=True)
        assert message != None
        assert message[0][1] == 'Twoja nazwa musi mieć conajmniej 3 znaki'
        
def test_password_mismatch():
    os.environ['FLASK_CONFIG'] = 'testing'
    flask_app = create_app(os.getenv('FLASK_CONFIG') or 'default')
    
    with flask_app.test_client() as test_client:
        response = test_client.post('/rejestracja', data=dict(email='test@test.com', name='Test', password1='passwrd', password2='password'))
        message = get_flashed_messages(with_categories=True)
        assert message != None
        assert message[0][1] == 'Hasła się nie zgadzają'
        
def test_password_too_short():
    os.environ['FLASK_CONFIG'] = 'testing'
    flask_app = create_app(os.getenv('FLASK_CONFIG') or 'default')
    
    with flask_app.test_client() as test_client:
        response = test_client.post('/rejestracja', data=dict(email='test@test.com', name='Test', password1='passwrd', password2='passwrd'))
        message = get_flashed_messages(with_categories=True)
        assert message != None
        assert message[0][1] == 'Hasło musi mieć conajmniej 8 znaków'
        
def test_correct_signup():
    os.environ['FLASK_CONFIG'] = 'testing'
    flask_app = create_app(os.getenv('FLASK_CONFIG') or 'default')
    
    with flask_app.test_client() as test_client:
        response = test_client.post('/rejestracja', data=dict(email='test@test.com', name='Test', password1='password', password2='password'))
        message = get_flashed_messages(with_categories=True)
        assert message != None
        assert message[0][1] == 'Wysłaliśmy link potwierdzający konto na Twój adres email'
        
def test_existing_user():
    os.environ['FLASK_CONFIG'] = 'testing'
    flask_app = create_app(os.getenv('FLASK_CONFIG') or 'default')
    
    with flask_app.test_client() as test_client:
        response = test_client.post('/rejestracja', data=dict(email='test@test.com', name='Test', password1='password', password2='password'))
        message = get_flashed_messages(with_categories=True)
        assert message != None
        assert message[0][1] == 'Już istnieje taki użytkownik'
        