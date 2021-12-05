from flask import Blueprint, render_template, redirect, url_for, request, flash

#routes related to authentication

auth = Blueprint("auth", __name__)

@auth.route("/login", methods=["GET", "POST"])
def login():
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

        database = ["luukas@gmail.com", "ltd"]

        if email in database:
            flash("Email already exits!", category="error")
        if username in database:
            flash("Username already exits!", category="error")
        if len(email) < 7:
            flash("Email is too short!", category="error")
        if len(username) < 3:
            flash("Username is too short!", category="error")
        if len(password) < 5:
            flash("Password is too short!", category="error")
        if password != password2:
            flash("Passwords don't match!", category="error")
        else:
            #add user to the database
            flash("User created!", category="success")
    
    return render_template("sign_up.html")
