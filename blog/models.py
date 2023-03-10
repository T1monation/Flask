from blog.app import db
from flask_login import UserMixin
import sqlalchemy


class User(db.Model, UserMixin):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True)
    name = db.Column(db.String(255))
    password = db.Column(db.String(255))
    psd = db.Column(db.String(255))
    articles = db.relationship("Article", backref="autors")
    is_admin = db.Column(db.Boolean, default=False)


class Article(db.Model):
    __table_name__ = "articles"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    text = db.Column(db.String)
    author_id = db.Column(db.Integer, db.ForeignKey("users.id"))
