from . import db 
from flask_login import UserMixin
from sqlalchemy.sql import func

class User(db.Model, UserMixin):
    __tablename__ = "users"
    
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(128), unique=True, nullable=False)
    password = db.Column(db.String(150))
    name = db.Column(db.String(150))
    active = db.Column(db.Boolean(), default=True, nullable=False)
    role = db.Column(db.String(20), default='User', nullable=False) 
    
    def __init__(self, email, name, password):
        self.email = email
        self.name = name
        self.password = password
        
        
class Systems(db.Model):
    __tablename__ = "systems"
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200))
        
class Campain(db.Model):
    __tablename__ = "campains"
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))
    system = db.Column(db.Integer, db.ForeignKey('systems.id'))
    description = db.Column(db.String(2000))
    session_number = db.Column(db.Integer, default=0, nullable=False)
    game_master = db.Column(db.Integer, db.ForeignKey('user.id'))
    

class PlayersCharacters(db.Model):
    __tablename__ = "playersCharacters"
    
    id = db.Column(db.Integer, primary_key=True)
    userId = db.Column(db.Integer, db.ForeignKey('user.id'))
    campainId = db.Column(db.Integer, db.ForeignKey('campains.id'))
    name = db.Column(db.String(100))
    system = db.Column(db.Integer, db.ForeignKey('systems.id'))
    exp = db.Column(db.Integer)
    

class StatsNeuroshima(db.Model):
    __tablename__ = "statsNeuroshima"
    
    id = db.Column(db.Integer, primary_key=True)
    

class Equipment(db.Model):
    __tablename__ = "equipment"
    
    id = db.Column(db.Integer, primary_key=True)
    itemId = db.Column(db.Integer, db.ForeignKey('items.id'))
    characterId = db.Column(db.Integer, db.ForeignKey('playersCharacters.id'))
    
    
class Items(db.Model):
    __tablename__ = "items"
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250))
    description = db.Column(db.String(2000))
    
    
class Tricks(db.Model):
    __tablename__ = "tricks"
    
    id = db.Column(db.Integer, primary_key=True)
    
    
class NPC(db.Model):
    __tablename__ = "NPC"
    
    id = db.Column(db.Integer, primary_key=True)
    
    
class CharactertsTricks(db.Model):
    __tablename__ = "charactersTricks"
    
    id = db.Column(db.Integer, primary_key=True)
