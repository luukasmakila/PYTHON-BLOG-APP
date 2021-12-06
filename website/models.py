from . import db
from flask_login import UserMixin #allows us to log users in and out easier
from sqlalchemy.sql import func #fills date created with current time

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    username = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(200))
    date = db.Column(db.date(Timezone=True), default = func.now())