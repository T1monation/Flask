from flask import Blueprint
from flask import render_template
from werkzeug.exceptions import NotFound
from flask import redirect
from blog.app import login_manager
from flask_login import login_required


user = Blueprint("user", __name__, static_folder="../static", url_prefix="/users")


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
    articles = Article.query.filter_by(author_id=pk).all()
    print(articles)
    return render_template("users/profile.html", user=user, articles=articles)
