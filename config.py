import os

class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATEBASE_URI = 'postgresql://roylai:nXSYgQnSp2EZSoKq0H3TxXRIKpvZGqJg@dpg-cjbik5vdb61s738d8jm0-a.singapore-postgres.render.com/a_ewvc'

class ProdConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATEBASE_URI = os.environ.get('SQLALCHEMY_DATEBASE_URI')