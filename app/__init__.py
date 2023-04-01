from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import config

#db = SQLAlchemy()
#DB_NAME = "database.db"

def create_app(config_name):
    app = Flask(__name__)
    
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    #db.init_app(app)
    
    from .view import views
    from .auth import auth
    
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    
    return app