from . import db 
from flask import current_app
import hashlib
from flask_login import UserMixin

class User(db.Model, UserMixin):
    __tablename__ = "users"
    
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(128), unique=True, nullable=False)
    password = db.Column(db.String(150))
    name = db.Column(db.String(150))
    active = db.Column(db.Boolean(), default=True, nullable=False)
    confirmed = db.Column(db.Boolean, default=False)
    role = db.Column(db.String(12), default='User')
    #avatarHash = db.Column(db.String(32))
    
    def __init__(self, email, name, password, role='User'):
        self.email = email
        self.name = name
        self.password = password
        self.confirmed = False
                 
        
class Campain(db.Model):
    __tablename__ = "campains"
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))
    description = db.Column(db.String(2000))
    session_number = db.Column(db.Integer, default=0, nullable=False)
    game_master = db.Column(db.Integer, db.ForeignKey('users.id'))
    

class UsersCampain(db.Model):
    __tablename__ = "usersCampains"
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    campain_id = db.Column(db.Integer, db.ForeignKey('campains.id'))

class NPC(db.Model):
    __tablename__ = "NPC"
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    location = db.Column(db.String(100))
    opinion = db.Column(db.String(200))
    description = db.Column(db.String(2000))
    campainId = db.Column(db.Integer, db.ForeignKey('campains.id'))
    avatarHash = db.Column(db.String(32))
