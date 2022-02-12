import os
class Config:
  """
  General configuration class
  """
SECRET_KEY= os.urandom(30)

class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}
