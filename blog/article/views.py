from flask import Blueprint
from flask import render_template
from werkzeug.exceptions import NotFound
from flask_login import login_required


article = Blueprint(
    "article", __name__, static_folder="../static", url_prefix="/article"
)


@article.route("/")
@login_required
def article_list():
    from blog.models import Article

    articles = Article.query.all()
    print(articles, 555555555)
    return render_template("articles/list.html", articles=articles)


@article.route("/<int:pk>")
@login_required
def get_article(pk: int):
    print(pk, 222222)
    from blog.models import Article, User

    try:
        article = Article.query.filter_by(id=pk).one_or_none()
    except KeyError:
        raise NotFound(f"Article id {pk} not found")
        # return redirect("/users/")
    author = User.query.filter_by(id=article.author_id).one_or_none()
    return render_template("articles/details.html", article=article, author=author)
