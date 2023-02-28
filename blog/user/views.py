from flask import Blueprint
from flask import render_template
from werkzeug.exceptions import NotFound
from flask import redirect


user = Blueprint("user", __name__, static_folder="../static", url_prefix="/users")


# USERS = ["Alice", "John", "Mike"]
USERS = {1: "Alice", 2: "John", 3: "Mike"}


@user.route("/")
def user_list():
    return render_template("users/list.html", users=USERS)


@user.route("/<int:pk>")
def get_user(pk: int):
    try:
        user_name = USERS[pk]
    except KeyError:
        raise NotFound(f"User id {pk} not found")
        # return redirect("/users/")
    return render_template("users/details.html", user_name=user_name)
