from blog.extensions import db
from mimesis import Person, Text
import click
from werkzeug.security import generate_password_hash
import random


@click.command("create-init-user")
def create_init_user(num=100):
    from blog.models import User, Article
    from wsgi import app

    with app.app_context():
        db.create_all()

    with app.app_context():
        person = Person()
        for el in range(num):
            paswd_str = person.password()
            db.session.add(
                User(
                    email=person.email(),
                    password=generate_password_hash(paswd_str),
                    psd=paswd_str,
                )
            )
        db.session.commit()

    with app.app_context():
        id_list = db.session.query(User.id).all()
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
