"""
Contains all the environment variables per build.
"""
import os


class Config:  # pylint: disable=too-few-public-methods
    """
    The default variables applied to all environments.
    """
    SECRET_KEY = os.urandom(16)
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = False


class DevelopmentConfig(Config):  # pylint: disable=too-few-public-methods
    """
    Variables that add to/overwrite values from the default class for the development environment.
    """
    SQLALCHEMY_DATABASE_URI = 'postgresql://james:whale@localhost/jameswhale'
    SQLALCHEMY_RECORD_QUERIES = True
    DEBUG = True


class TestingConfig(Config):  # pylint: disable=too-few-public-methods
    """
    Variables that add to/overwrite values from the default class for the testing environment.
    """
    SQLALCHEMY_DATABASE_URI = 'postgresql://james:whale@localhost/jameswhale'
    TESTING = True
    WTF_CSRF_ENABLED = False


class ProductionConfig(Config):  # pylint: disable=too-few-public-methods
    """
    Variables that add to/overwrite values from the default class for the production environment.
    """
    SQLALCHEMY_DATABASE_URI = 'postgresql://james:whale@database/jameswhale'
    DEBUG = False


config_by_name = dict(
    dev=DevelopmentConfig,
    test=TestingConfig,
    prod=ProductionConfig
)
