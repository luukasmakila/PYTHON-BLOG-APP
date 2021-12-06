from flask import Flask
from flask_sqlalchemy import SQLAlchemy

#creates the app

db = SQLAlchemy()
DB = "database.db"

def create_app():
    app = Flask(__name__)
    app.secret_key = "adasfdsfgsv"
    app.config["SQL_ALCHEMY_DATABASE_URI"] = f"sqlite://{DB}"
    db.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")

    from .models import User
    
    create_database(app)
    
    return app

def create_database(app):
    if not path.exists("website/"+DB):
        db.create_all(app=app)
