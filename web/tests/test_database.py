import os
from app import create_app, db
from app.model import User, Campain, UsersCampain
from werkzeug.security import check_password_hash

os.environ['FLASK_CONFIG'] = 'testing'
flask_app = create_app(os.getenv('FLASK_CONFIG') or 'default')

def test_User_table():
    with flask_app.app_context():
        user = db.session.query(User).filter(User.name == 'Tytus').first()
        assert user.email == 'tytus@test.com'
        assert check_password_hash(user.password, 'password') == True
        
def test_Campain_table():
    with flask_app.app_context():
        campain = db.session.query(Campain).filter(Campain.name == 'test1').first()
        assert campain.game_master == 2
        
def test_UsersCampain_table():
    with flask_app.app_context():
        users_campain = db.session.query(UsersCampain).filter(UsersCampain.id == 1).first()
        assert users_campain.user_id == 1
        assert users_campain.campain_id == 1