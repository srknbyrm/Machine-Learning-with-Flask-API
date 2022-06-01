import os

class Config(object):
    DEBUG = False
    TESTING = False
    SECRET_KEY = os.urandom(32)  # For using in CSRF Protection
    TITLE = "ToolBox"


class ProductionConfig(Config):
    DEBUG = False
    TESTING = False
    SECRET_KEY = os.urandom(32)
    TITLE = "ToolBox"


class DevelopmentConfig(Config):
    DEBUG = True
    TESTING = False
    SECRET_KEY = os.urandom(32)
    TITLE = "ToolBox"


class TestingConfig(Config):
    DEBUG = True
    TESTING = True
    SECRET_KEY = os.urandom(32)
    TITLE = "ToolBox"
