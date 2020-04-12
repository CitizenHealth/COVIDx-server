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


app_config = {
    "development": DevelopmentConfig,
    "production": ProductionConfig,
    "testing": TestingConfig
}