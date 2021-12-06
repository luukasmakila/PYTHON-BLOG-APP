from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

#creates the app

db = SQLAlchemy()
DB = "database.db"

def create_app():
    app = Flask(__name__)
    app.secret_key = "adasfdsfgsv"
    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{DB}"
    db.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")

    from .models import User

    create_database(app)

    login_manager = LoginManager() #allows to log users in and out and check if they are logged in or not
    login_manager.login_view = "auth.login" #if not logged in, redirects to the login page
    login_manager.init_app(app)

    @login_manager.user_loader #allows us to access the users id thats in a current session
    def load_user(id):
        User.query.get(int(id))
    
    return app

def create_database(app):
    if not path.exists("website/"+DB):
        db.create_all(app=app)
