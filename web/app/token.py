from itsdangerous import URLSafeTimedSerializer as Serializer
from flask import current_app

  
def generate_confirmation_token(email):
    s = Serializer(current_app.config['SECRET_KEY'])
    return s.dumps(email, salt=current_app.config['SECRET_KEY'])
    
def confirm_account(token, expiration=3600):
    s = Serializer(current_app.config['SECRET_KEY'])
    try:
        email = s.loads(
            token,
            salt=current_app.config['SECRET_KEY'],
            max_age=expiration
        )
    except:
        return False
    return email