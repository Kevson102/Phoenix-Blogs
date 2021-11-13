import os
class Config:
  SECRET_KEY = os.environ.get('SECRET_KEY')
  SQLALCHEMY_DATABASE_URL = 'postgresql+psycopy2://kevson:Antidolofinomonoligasta102@localhost/blogs'
  UPLOADED_PHOTOS_DEST ='app/static/photos'

  
  
class ProdConfig(Config):
  '''
  Production Configuration child class
  Args:
    Config: The parent configuration class with general configuration settings
  '''
  pass


class DevConfig(Config):
  '''
  Development configuration child class.
  Args:
    Config: The parent configuration class with general configuration settings
  '''
  SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://kevson:Antidolofinomonoligasta102@localhost/blogs'

  DEBUG = True
  
config_options = {
  'development' : DevConfig,
  'production' : ProdConfig
}