from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user
from . models import Post
from . import db

#routes related to views

views = Blueprint("views", __name__)

@views.route("/")
@login_required
def home():
    posts = Post.query.all()
    return render_template("home.html", user=current_user, posts=posts)

@views.route("/create-post", methods=["GET", "POST"])
@login_required
def create_post():
    if request.method == "POST":
        text = request.form.get("text")
        if not text:
            flash("Can't make an empty post!", category="error")
        else:
            post = Post(text=text, creator=current_user.id)
            db.session.add(post)
            db.session.commit()
            flash("Post created", category="success")
            return redirect(url_for("views.home"))

    return render_template("create_post.html", user=current_user)