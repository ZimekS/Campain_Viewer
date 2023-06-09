import os
from app import create_app


def test_home_page():
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
        response = test_client.get('/')
        assert response.status_code == 200
        assert b"This is home" in response.data
        
def test_MG_campains_page():

    os.environ['FLASK_CONFIG'] = 'testing'
    flask_app = create_app(os.getenv('FLASK_CONFIG') or 'default')

    
    with flask_app.test_client() as test_client:
        response = test_client.get('/prowadzisz')
        assert response.status_code == 200
        assert b"Na tej stronie zobaczysz wszystkie kampanie" in response.data

def test_player_campains_page():

    os.environ['FLASK_CONFIG'] = 'testing'
    flask_app = create_app(os.getenv('FLASK_CONFIG') or 'default')

    
    with flask_app.test_client() as test_client:
        response = test_client.get('/grasz')
        assert response.status_code == 200
        assert b"Grasz w ..." in response.data