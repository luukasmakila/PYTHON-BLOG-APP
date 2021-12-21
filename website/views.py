from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask.scaffold import F
from flask_login import login_required, current_user
from . models import Post, User, Comment, Like, Dislike
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

@views.route("/delete-post/<id>")
@login_required
def delete_post(id):
    post = Post.query.filter_by(id=id).first()

    if not post:
        flash("Post doesn't exist!", category="error")
    elif current_user.id != post.creator:
        flash("You are not the creator of this post!", category="error")
    else:
        db.session.delete(post)
        db.session.commit()
        flash("Post deleted!", category="success")

    return redirect(url_for("views.home"))

@views.route("/posts/<username>")
@login_required
def posts(username):
    user = User.query.filter_by(username=username).first()

    if not user:
        flash("No user with this username!", category="error")
        return redirect(url_for("views.home"))

    posts = user.posts
    return render_template("posts.html", user=current_user, posts=posts, username=username)

@views.route("/create-comment/<post_id>", methods=["POST"])
@login_required
def create_comment(post_id):
    text = request.form.get("text")

    if not text:
        flash("Can't post an empty comment!", category="error")
    else:
        post = Post.query.filter_by(id=post_id)
        if post:
            comment = Comment(text=text, creator=current_user.id, post_id=post_id)
            db.session.add(comment)
            db.session.commit()
            flash("Comment added successfully!", category="success")
        else:
            flash("Post doesn't exist!", category="error")
    return redirect(url_for("views.home"))

@views.route("/delete-comment/<id>")
@login_required
def delete_comment(id):
    comment = Comment.query.filter_by(id=id).first()

    if not comment:
        flash("Comment doesn't exist!", category="error")
    elif current_user.id != comment.creator and current_user.id != comment.post.creator:
        flash("You are not the creator of this comment!", category="error")
    else:
        db.session.delete(comment)
        db.session.commit()
        flash("Comment deleted!", category="success")

    return redirect(url_for("views.home"))

@views.route("/like-post/<post_id>", methods=["GET"])
@login_required
def like(post_id):
    post = Post.query.filter_by(id=post_id)
    like = Like.query.filter_by(creator=current_user.id, post_id=post_id).first()
    dislike = Dislike.query.filter_by(creator=current_user.id, post_id=post_id).first()

    if not post:
        flash("Post doesn't exist!", category="error")
    elif dislike:
        flash("Can not dislike a post you've already liked!", category="error")
    elif like:
        db.session.delete(like)
        db.session.commit()
    else:
        like = Like(creator=current_user.id, post_id=post_id)
        db.session.add(like)
        db.session.commit()
    return redirect(url_for("views.home"))

@views.route("/dislike-post/<post_id>", methods=["GET"])
@login_required
def dislike(post_id):
    post = Post.query.filter_by(id=post_id)
    dislike = Dislike.query.filter_by(creator=current_user.id, post_id=post_id).first()
    like = Like.query.filter_by(creator=current_user.id, post_id=post_id).first()

    if not post:
        flash("Post doesn't exist!", category="error")
    elif like:
        flash("Can not dislike a post you've already liked!", category="error")
    elif dislike:
        db.session.delete(dislike)
        db.session.commit()
    else:
        dislike = Dislike(creator=current_user.id, post_id=post_id)
        db.session.add(dislike)
        db.session.commit()
    return redirect(url_for("views.home"))