import os
class Config:
  SECRET_KEY = os.environ.get('SECRET_KEY')
  UPLOADED_PHOTOS_DEST ='app/static/photos'
  QUOTE_API_BASE_URL = 'http://quotes.stormconsultancy.co.uk/random.json'

  
  
class ProdConfig(Config):
  '''
  Production Configuration child class
  Args:
    Config: The parent configuration class with general configuration settings
  '''
  SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")


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