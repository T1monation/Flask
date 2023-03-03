from blog.app import create_app, db
from werkzeug.security import generate_password_hash
from mimesis import Person, Text
import random

app = create_app()


@app.cli.command("init-db")
def init_db():
    """
    Run in your terminal:
    flask init-db
    """
    db.create_all()
    print("Done!")


@app.cli.command("create-users")
def create_users(num=100):
    from blog.models import User

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
    print("Users creation done!")


@app.cli.command("create-articles")
def create_articles(num=300):
    from blog.models import User, Article

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
    print("Articles creation done!")
