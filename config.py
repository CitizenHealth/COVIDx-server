
class Config(object):
    """
    any configs that we run always
    """


class DevelopmentConfig(Config):
    """
    dev config
    """

    DEBUG=True
    SQLALCHEMY_ECHO=True


class ProductionConfig(Config):
    """
    prod config
    """

    DEBUG=False




app_config = {
    "development": DevelopmentConfig,
    "production": ProductionConfig,
}