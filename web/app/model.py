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
    game_master = db.Column(db.Integer, db.ForeignKey('users.id'))
    

class PlayersCharacters(db.Model):
    __tablename__ = "playersCharacters"
    
    id = db.Column(db.Integer, primary_key=True)
    userId = db.Column(db.Integer, db.ForeignKey('users.id'))
    campainId = db.Column(db.Integer, db.ForeignKey('campains.id'))
    name = db.Column(db.String(100))
    system = db.Column(db.Integer, db.ForeignKey('systems.id'))
    neuroStatsId = db.Column(db.Integer, db.ForeignKey('statsNeuroshima.id'), nullable=True)
    ddStatsId = db.Column(db.Integer, db.ForeignKey('statsDD.id'), nullable=True)
    exp = db.Column(db.Integer)
    
    #@hybrid_property
    def stats_id(self):
        return self.neuroStatsId or self.ddStatsId
    
class StatsNeuroshima(db.Model):
    __tablename__ = "statsNeuroshima"
    
    id = db.Column(db.Integer, primary_key=True)
    agility = db.Column(db.Integer)
    perception = db.Column(db.Integer)
    charisma = db.Column(db.Integer)
    flair = db.Column(db.Integer)
    build = db.Column(db.Integer)

class StatsDD(db.Model):
    __tablename__ = "statsDD"
    
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
    name = db.Column(db.String(100))
    location = db.Column(db.String(100))
    opinion = db.Column(db.String(200))
    description = db.Column(db.String(2000))
    campainId = db.Column(db.Integer, db.ForeignKey('campains.id'))
    avatarHash = db.Column(db.String(32))
  
class CharactertsTricks(db.Model):
    __tablename__ = "charactersTricks"
    
    id = db.Column(db.Integer, primary_key=True)
