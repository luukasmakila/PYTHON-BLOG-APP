from . import db
from flask_login import UserMixin #allows us to log users in and out easier
from sqlalchemy.sql import func #fills date created with current time

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    username = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(200))
    date = db.Column(db.DateTime(timezone=True), default = func.now())
    posts = db.relationship("Post", backref="user", passive_deletes=True) #refereneces all of the users posts

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime(timezone=True), default = func.now())
    creator = db.Column(db.Integer, db.ForeignKey("user.id", ondelete="CASCADE"), nullable=False) #when user is deleted all of their posts will be deleted aswell.