import logging


class Config:
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///jouerfluxDB.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    LOG_FILE = 'logs/myapp.log'
    LOG_LEVEL = logging.DEBUG
    LOG_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'


class DevelopmentConfig(Config):
    DEBUG = True
