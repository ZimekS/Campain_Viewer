import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'sh5ofiobxxz808dfh39d'
    SECURITY_PASSWORD_SALT = '#w6!f'
    MAIL_SERVER = os.environ.get('MAIL_SERVER', 'smtp.gmail.com')
    MAIL_PORT = int(os.environ.get('MAIL_PORT', '587'))
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False
    #MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS', 'true').lower()
    #MAIL_USE_SSL = os.environ.get('MAIL_USE_SSL', 'false').lower()
    MAIL_USERNAME = 'zimekpol@gmail.com'
    #MAIL_PASSWORD = 'tidaJuru-ne'
    MAIL_PASSWORD = 'lcylsrjgcoxoyzzz'
    #FLASKY_MAIL_SUBJECT_PREFIX = '[Flasky]'
    #FLASKY_MAIL_SENDER = 'Flasky Admin <flasky@przyklad.pl>'
    FLASKY_ADMIN = 'zimekpol@gmail.com'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    @staticmethod
    def init_app(app):
        pass
    
class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL')
    
class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL')
    
class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
   
    
config = { 'development': DevelopmentConfig, 'testing': TestingConfig, 'production': ProductionConfig, 'default': DevelopmentConfig}