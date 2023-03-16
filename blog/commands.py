from blog.extensions import db
from mimesis import Person, Text, Internet
import click
from werkzeug.security import generate_password_hash
import random


@click.command("create-fake-data")
def create_fake_data(num=100):
    from blog.models import User, Article, Author, Tag
    from wsgi import app

    with app.app_context():
        person = Person()
        for el in range(num):
            paswd_str = person.password()
            db.session.add(
                User(
                    email=person.email(),
                    first_name=person.name(),
                    last_name=person.last_name(),
                    password=generate_password_hash(paswd_str),
                    psd=paswd_str,
                )
            )
        db.session.commit()

    with app.app_context():
        id_list = db.session.query(User.id).all()
        id_list_normal = [el[0] for el in id_list]
        for el in id_list_normal:
            if random.randrange(0, 2, 1) == 1:
                db.session.add(Author(users_id=el))
        db.session.commit()

    with app.app_context():
        id_list = db.session.query(Author.id).all()
        id_list_normal = [el[0] for el in id_list]
        text_obj = Text()
        for el in range(num * 2):
            db.session.add(
                Article(
                    title=text_obj.title(),
                    text=text_obj.text(),
                    author_id=random.choice(id_list_normal),
                )
            )
        db.session.commit()

    with app.app_context():
        tag = Internet()
        for el in range(20):
            db.session.add(Tag(name=tag.hashtags(1)))
        db.session.commit()


@click.command("create-tag")
def create_tag():
    from blog.models import Article, Tag
    from wsgi import app

    with app.app_context():
        tag_list = Tag.query.all()
        article_list = Article.query.all()
        for article in article_list:
            for el in range(random.randint(1, 5)):
                article.tag.append(random.choice(tag_list))
        db.session.commit()


@click.command("create-admin")
def create_admin():
    from blog.models import User
    from blog.extensions import db

    user_email = input("Input user email: ")
    admin_candidate = User.query.filter_by(email=user_email).one_or_none()
    if admin_candidate:
        admin_candidate.is_admin = True
        db.session.commit()
    else:
        print("User dosn't exist!")
