from flask import Blueprint
from flask import render_template
from werkzeug.exceptions import NotFound


article = Blueprint(
    "article", __name__, static_folder="../static", url_prefix="/article"
)


ARTICLES = {
    1: {
        "text": "Lorem ipsum dolor sit amet consectetur adipisicing elit. Consectetur, quasi?",
        "author": 1,
        "title": "1111",
    },
    2: {
        "text": "Lorem, ipsum dolor sit amet consectetur adipisicing elit. Corrupti dignissimos sunt qui cum laboriosam quisquam.",
        "author": 2,
        "title": "2222",
    },
    3: {
        "text": "Lorem ipsum dolor sit amet consectetur.",
        "author": 1,
        "title": "3333",
    },
}


@article.route("/")
def article_list():
    return render_template("articles/list.html", articles=ARTICLES)


@article.route("/<int:pk>")
def get_article(pk: int):
    try:
        article_body = ARTICLES[pk]
    except KeyError:
        raise NotFound(f"Article id {pk} not found")
        # return redirect("/users/")
    return render_template("articles/details.html", article_body=article_body)
