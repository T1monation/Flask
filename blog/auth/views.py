from flask import Blueprint, flash, redirect, url_for
from flask import render_template, request
from werkzeug.security import check_password_hash
from flask_login import logout_user, login_user, login_required
from blog.app import login_manager

auth = Blueprint("auth", __name__, static_folder="../static")


@auth.route(
    "/login",
    methods=["POST", "GET"],
)
def login():
    if request.method == "GET":
        return render_template("auth/login.html")
    email = request.form.get("email")
    password = request.form.get("password")
    from blog.models import User

    user = User.query.filter_by(email=email).first()
    if not user or not check_password_hash(user.password, password):
        flash("Check your login details")
        return redirect(url_for(".login"))

    login_user(user)
    print(user.is_anonymous)
    print(user.id)
    return redirect(url_for("user.profile", pk=user.id))


@auth.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for(".login"))


@auth.route("/authcheck")
def auth_check():
    return render_template("auth/authcheck.html")
