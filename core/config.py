import os

class Config:
    SECRET_KEY = '5791628bb0b13ce0c676dfde280ba245' #os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'mysql://ptuser:Bs5tcYJzPowJHoI@mysql-ptc/ptc' #'sqlite:///site.db' #os.environ.get('SQLALCHEMY_DATABASE_URI')
    #MAIL_SERVER = 'smtp.googlemail.com'
    #MAIL_PORT = 587
    #MAIL_USE_TLS = True
    #MAIL_USERNAME = os.environ.get('EMAIL_USER')
    #MAIL_PASSWORD = os.environ.get('EMAIL_PASS')

    # JWT config
    JWT_TOKEN_LOCATION = ["cookies"]
    JWT_COOKIE_SECURE = True
    JWT_SECRET_KEY = "asdiufytasdfuiytasfyuitasdfuiyta"
    JWT_COOKIE_CSRF_PROTECT = False
    SERVER_NAME="api.ptcore.test"