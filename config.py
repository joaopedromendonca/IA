from dotenv import load_dotenv
from os import environ, path

base_dir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(base_dir, ".env"), override=True)


class Config(object):

    SECRET_KEY = "Q*[\\!o\xd6\xe5v\xcd\xaa]F\xfb\xe0\xb0\xe3\x8f\xfb\xcf\xf1j\xa8>"
    FLASK_APP = "wsgi.py"

    DEBUG = True
    TESTING = False

    STATIC_FOLDER = "static"
    TEMPLATES_FOLDER = "templates"

    SQLALCHEMY_DATABASE_URI = (
        "mysql+pymysql://root:123@127.0.0.1:3306/tictactoedb"
    )
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    SESSION_COOKIE_SECURE = True


class ProductionConfig(Config):
    pass


class DevelopmentConfig(Config):

    DEBUG = True

    SESSION_COOKIE_SECURE = False


class TestingConfig(Config):

    TESTING = True

    SESSION_COOKIE_SECURE = False
