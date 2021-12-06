from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_user, logout_user, login_required
from . import db
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash

#routes related to authentication

auth = Blueprint("auth", __name__)

@auth.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        database = ["luukas@gmail.com", "ltd"]

        if email not in database:
            flash("No users with the given email!", category="error")
        if not password: #if the password is not correct
            flash("Wrong password!", category="error")
        else:
            #log the user in
            flash("Successfully logged in!", category="success")
    
    return render_template("login.html")

@auth.route("/logout")
def logout():
    return redirect(url_for("views.home")) #redirects user to the home page

@auth.route("/sign-up", methods=["GET", "POST"])
def sign_up():

    if request.method == "POST":
        email = request.form.get("email")
        username = request.form.get("username")
        password = request.form.get("password")
        password2 = request.form.get("password2")

        email_exists = User.query.filter_by(email=email).first()
        username_exists = User.query.filter_by(username=username).first()

        if email_exists:
            flash("Email already exits!", category="error")
        elif username_exists:
            flash("Username already exits!", category="error")
        elif len(email) < 7:
            flash("Email is too short!", category="error")
        elif len(username) < 3:
            flash("Username is too short!", category="error")
        elif len(password) < 5:
            flash("Password is too short!", category="error")
        elif password != password2:
            flash("Passwords don't match!", category="error")
        else:
            newUser = User(email=email, username=username, password=generate_password_hash(password, method="sha256"))
            db.session.add(newUser) #makes user ready to be added to the DB
            db.session.commit() #commits the adding of the user to the DB
            flash("User created!", category="success")
            return redirect(url_for("views.home"))
    
    return render_template("sign_up.html")
