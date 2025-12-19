from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from .config import Config

db = SQLAlchemy()
jwt = JWTManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config())

    CORS(app, supports_credentials=True)  # Enable CORS with credentials support

    # Configure JWT cookies for cross-origin (localhost ports)
    app.config['JWT_ACCESS_COOKIE_SAMESITE'] = 'None'
    app.config['JWT_ACCESS_COOKIE_SECURE'] = False  # Allow over HTTP in development

    db.init_app(app)
    jwt.init_app(app)

    from .routes.auth import auth_bp
    from .routes.profile import profile_bp

    app.register_blueprint(auth_bp, url_prefix='/api/auth')
    app.register_blueprint(profile_bp, url_prefix='/api/profile')

    return app