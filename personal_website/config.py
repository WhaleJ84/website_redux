class Config:
    SECRET_KEY = '\xa5\xff\xe67\xa5\x85\x9cd\xe6=\xa1]\xb6C \xcd\x10\xfdl\xa9\xe2^Dz'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = False


class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql://james:whale@localhost/jameswhale'
    SQLALCHEMY_RECORD_QUERIES = True
    DEBUG = True


class TestingConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql://james:whale@localhost/jameswhale'
    TESTING = True
    WTF_CSRF_ENABLED = False


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql://james:whale@database/jameswhale'
    DEBUG = False


config_by_name = dict(
    dev=DevelopmentConfig,
    test=TestingConfig,
    prod=ProductionConfig
)
