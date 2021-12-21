from . import db
from flask_login import UserMixin #allows us to log users in and out easier
from sqlalchemy.sql import func #fills date created with current time

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    username = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(200))
    date = db.Column(db.DateTime(timezone=True), default = func.now())
    posts = db.relationship("Post", backref="user", passive_deletes=True) #refereneces all of the users posts, one to many relationship
    comments = db.relationship("Comment", backref="user", passive_deletes=True)
    likes = db.relationship("Like", backref="user", passive_deletes=True)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime(timezone=True), default = func.now())
    creator = db.Column(db.Integer, db.ForeignKey("user.id", ondelete="CASCADE"), nullable=False) #when user is deleted all of their posts will be deleted aswell.
    comments = db.relationship("Comment", backref="post", passive_deletes=True)
    likes = db.relationship("Like", backref="post", passive_deletes=True)

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(150), nullable=False)
    date = db.Column(db.DateTime(timezone=True), default = func.now())
    creator = db.Column(db.Integer, db.ForeignKey("user.id", ondelete="CASCADE"), nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey("post.id", ondelete="CASCADE"), nullable=False)

class Like(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    creator = db.Column(db.Integer, db.ForeignKey("user.id", ondelete="CASCADE"), nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey("post.id", ondelete="CASCADE"), nullable=False)
    date = db.Column(db.DateTime(timezone=True), default = func.now())