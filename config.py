import os

class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://roylai:nXSYgQnSp2EZSoKq0H3TxXRIKpvZGqJg@dpg-cjbik5vdb61s738d8jm0-a.singapore-postgres.render.com/a_ewvc'

class ProdConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')