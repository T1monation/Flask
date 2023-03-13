from flask import Blueprint, render_template, url_for
from blog.models import Author

author = Blueprint("author", __name__, static_folder="../static", url_prefix="/authors")


@author.route("/")
def author_list():
    authors = Author.query.all()
    return render_template("author/list.html", authors=authors)
