from blog.app import db
from flask_login import UserMixin
import sqlalchemy


class User(db.Model, UserMixin):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True)
    first_name = db.Column(db.String(255))
    last_name = db.Column(db.String(255))
    password = db.Column(db.String(255))
    psd = db.Column(db.String(255))
    articles = db.relationship("Article", backref="autors")
    is_admin = db.Column(db.Boolean, default=False)

    def __init__(self, email, first_name, last_name, password, psd, is_admin=False):
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.password = password
        self.psd = psd
        self.is_admin = is_admin


class Article(db.Model):
    __table_name__ = "articles"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    text = db.Column(db.String)
    author_id = db.Column(db.Integer, db.ForeignKey("users.id"))

    def __init__(self, title, text, author_id):
        self.title = title
        self.text = text
        self.author_id = author_id
