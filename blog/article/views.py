from flask import Blueprint, redirect, url_for, request
from flask import render_template
from werkzeug.exceptions import NotFound
from flask_login import login_required, current_user
from blog.forms.article import ArticleCreateForm
from blog.models import Article, Author
from blog.extensions import db
from psycopg2 import IntegrityError


article = Blueprint(
    "article", __name__, static_folder="../static", url_prefix="/article"
)


@article.route("/")
@login_required
def article_list():
    from blog.models import Article

    articles = Article.query.all()
    return render_template("articles/list.html", articles=articles)


@article.route("/<int:pk>")
@login_required
def get_article(pk: int):
    try:
        article = Article.query.filter_by(id=pk).one_or_none()
    except KeyError:
        raise NotFound(f"Article id {pk} not found")

    return render_template("articles/details.html", article=article)


@article.route("create", methods=["GET", "POST"])
@login_required
def create_article():
    form = ArticleCreateForm(request.form)
    errors = []

    if request.method == "POST" and form.validate_on_submit():
        _article = Article(title=form.title.data, text=form.text.data)

        if not current_user.author:
            author = Author(users_id=current_user.id)
            db.session.add(author)
            db.session.commit()

        _article.author_id = current_user.author.id
        db.session.add(_article)
        try:
            db.session.commit()
        except IntegrityError:
            errors.append("Some DB error")
        else:
            return redirect(url_for("article.get_article", pk=_article.id))

    return render_template("articles/create_article.html", form=form, errors=errors)
