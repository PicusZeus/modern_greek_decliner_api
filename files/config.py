import os

class Config(object):
    DEBUG = False
    TESTING = False
    SECRET_KEY = "αλφαβήτο"
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI', 'sqlite:///data.db')
    PROPAGATE_EXCEPTIONS = True
    JWT_BLACKLIST_ENABLED = True
    JWT_BLACKLIST_TOKEN_CHECKS = True
    ADMIN = 'picus-zeus'



class ProductionConfig(Config):
    pass

class DevelopmentConfig(Config):
    DEBUG = True



class TestingConfig(Config):
    TESTING = True


    SESSION_COOKIE_SECURE = False