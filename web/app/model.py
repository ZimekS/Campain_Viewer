from . import db 
from flask_login import UserMixin
from sqlalchemy.sql import func

class User(db.Model, UserMixin):
    __tablename__ = "users"
    
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(128), unique=True, nullable=False)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    active = db.Column(db.Boolean(), default=True, nullable=False)
    
    def __init__(self, email):
        self.email = email