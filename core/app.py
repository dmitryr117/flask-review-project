from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from core.config import Config
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from flask_wtf.csrf import CSRFProtect

from resources.files import UploadImage

db = SQLAlchemy()
bcrypt = Bcrypt()
api = Api()
jwt = JWTManager()
csrf_protect = CSRFProtect()
# jwt = JWT(app, authenticate, identity)

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    CORS( app, 
        origins=["https://api.ptcore.test", "https://ptcore.test", "https://client.ptcore.test"],
        supports_credentials=True)
    #CORS(app, origins=origins=["https://api.ptcore.test", "https://ptcore.test"]).

    db.init_app(app)
    bcrypt.init_app(app)
    jwt.init_app(app)

    # csrf_protect.init_app(app)
    # api = restful.Api(app, decorators=[csrf_protect.exempt])

    from controllers.users.auth import users
    app.register_blueprint(users)

    # Api Resources
    # api.decorators=[csrf_protect.exempt]
    api.add_resource(UploadImage, '/images')
    api.init_app(app)

    return app
