class Config(object):
    """
    any configs that we run always
    """
    DEBUG=True


class DevelopmentConfig(Config):
    """
    dev config
    """

    SQLALCHEMY_ECHO=True
    SQLALCHEMY_DATABASE_URI = 'mysql://admin@localhost/covidx_db'


class ProductionConfig(Config):
    """
    prod config
    """
    DEBUG=False


class TestingConfig(Config):
    """
    configurations for testing
    """
    TESTING=True
    SQLALCHEMY_DATABASE_URI = 'mysql://admin@localhost/covidx_db'


app_config = {
    "development": DevelopmentConfig,
    "production": ProductionConfig,
    "testing": TestingConfig
}