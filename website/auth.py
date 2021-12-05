from flask import Blueprint, render_template, redirect, url_for, request

#routes related to authentication

auth = Blueprint("auth", __name__)

@auth.route("/login", methods=["GET", "POST"])
def login():
    email = request.form.get("email")
    password = request.form.get("password")
    print(email)
    return render_template("login.html")

@auth.route("/logout")
def logout():
    return redirect(url_for("views.home")) #redirects user to the home page

@auth.route("/sign-up", methods=["GET", "POST"])
def sign_up():
    email = request.form.get("email")
    username = request.form.get("username")
    password = request.form.get("password")
    password2 = request.form.get("password2")
    print(username)
    return render_template("sign_up.html")
