from flask import Flask

#creates the app

def create_app():
    app = Flask(__name__)
    app.secret_key = "adasfdsfgsv"

    return app