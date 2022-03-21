from flask import Flask
from flask_login import LoginManager
from flask_login.config import USE_SESSION_FOR_NEXT
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_wtf.csrf import CSRFProtect
import datetime
import os
import config


db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()
csrf = CSRFProtect()

REMEMBER_COOKIE_DURATION = datetime.timedelta(minutes=5)
USE_SESSION_FOR_NEXT = True


@login_manager.user_loader
def load_user(user_id):
    
    from app.app_models import User
    
    if user_id is not None:
        return db.session.query(User).filter(User.id == user_id).first()
    return None


def create_app(testing=False):
    
    app = Flask(__name__)

    flask_env = os.getenv("FLASK_ENV",None)
    
    if testing:
        app.config.from_object(config.TestingConfig)
    elif flask_env == "development":
        app.config.from_object(config.DevelopmentConfig)
    elif flask_env == "testing":
        app.config.from_object(config.TestingConfig)
    else:
        app.config.from_object(config.ProductionConfig)
        
    db.init_app(app)
    login_manager.init_app(app)
    csrf.init_app(app)
    migrate.init_app(app)
    
    app.config["WTF_CSRF_TIME_LIMIT"] = 36000
    
    login_manager.login_view = "main.home"
    login_manager.needs_refresh_message = "Session timed out, please login again."
    login_manager.needs_refresh_message_category = "info"
    
    with app.app_context():
        
        from app.views import auth, public
        from app import app_models
        
        app.register_blueprint(auth.auth_bp)
        app.register_blueprint(public.public_bp)
        
        db.create_all()
        
        return app