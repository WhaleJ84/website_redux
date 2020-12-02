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
    Development will typically be run locally.
    """
    SQLALCHEMY_DATABASE_URI = f"{os.getenv('DEV_DB_URI')}"
    SQLALCHEMY_RECORD_QUERIES = True
    DEBUG = True


class TestingConfig(Config):  # pylint: disable=too-few-public-methods
    """
    Variables that add to/overwrite values from the default class for the testing environment.
    Testing will typically be run in a container.
    """
    SQLALCHEMY_DATABASE_URI = f"{os.getenv('TEST_DB_URI')}"
    TESTING = True
    WTF_CSRF_ENABLED = False


class ProductionConfig(Config):  # pylint: disable=too-few-public-methods
    """
    Variables that add to/overwrite values from the default class for the production environment.
    Production will typically be run bare on a server.
    """
    SQLALCHEMY_DATABASE_URI = f"{os.getenv('PROD_DB_URI')}"
    DEBUG = False


config_by_name = dict(
    dev=DevelopmentConfig,
    test=TestingConfig,
    prod=ProductionConfig
)
