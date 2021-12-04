from flask import Flask

#creates the app

def create_app():
    app = Flask(__name__)
    app.secret_key = "adasfdsfgsv"

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")
    
    return app