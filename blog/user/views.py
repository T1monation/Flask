from flask import Blueprint
from flask import render_template, url_for
from werkzeug.exceptions import NotFound
from werkzeug.security import generate_password_hash
from flask import redirect
from blog.app import login_manager
from flask_login import login_required, current_user, login_user
from blog.forms.user import UserRegisterForm
from flask import request
from blog.models import User
from blog.extensions import db
from psycopg2 import IntegrityError
import requests
from blog.config import API_URL


user = Blueprint("user", __name__, static_folder="../static",
                 url_prefix="/users")


@user.route("/")
def user_list():
    from blog.models import User

    users = User.query.all()
    return render_template("users/list.html", users=users)


@user.route("/<int:pk>")
@login_required
def profile(pk: int):
    from blog.models import User, Article

    user = User.query.filter_by(id=pk).one_or_none()
    if not user:
        raise NotFound(f"User #{pk} dosen't exist!")

    if user.author:
        users_articles_count = requests.get(
            f'{API_URL}/api/articles/{user.author.id}/event_get_count_by_author/').json()
        return render_template("users/profile.html", user=user, users_articles_count=users_articles_count['method'])
    else:
        return render_template("users/profile.html", user=user, users_articles_count=0)


@user.route("register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for("user.profile", pk=current_user.id))

    form = UserRegisterForm(request.form)
    errors = []

    if request.method == "POST" and form.validate_on_submit():
        if User.query.filter_by(email=form.email.data).count():
            form.email.errors.append("email not uniq")
            return render_template("users/register.html", form=form)

        _user = User(
            email=form.email.data,
            first_name=form.first_name.data,
            last_name=form.last_name.data,
            password=generate_password_hash(form.password.data),
            psd=form.password.data,
        )

        db.session.add(_user)
        try:
            db.session.commit()
        except IntegrityError:
            errors.append("Some DB error")
        else:
            login_user(_user)
            return redirect(url_for("user.profile", pk=current_user.id))

    return render_template("users/register.html", form=form, errors=errors)
