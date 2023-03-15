from blog.app import db
from flask_login import UserMixin
from sqlalchemy import ForeignKey, Table
from sqlalchemy.orm import relationship
from datetime import datetime


class User(db.Model, UserMixin):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True)
    first_name = db.Column(db.String(255))
    last_name = db.Column(db.String(255))
    password = db.Column(db.String(255))
    psd = db.Column(db.String(255))
    is_admin = db.Column(db.Boolean, default=False)

    author = relationship("Author", uselist=False, back_populates="user")


class Article(db.Model):
    __tablename__ = "articles"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    text = db.Column(db.String)
    author_id = db.Column(db.Integer, db.ForeignKey("authors.id"), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )

    author = relationship("Author", back_populates="article")
    tag = relationship(
        "Tag", secondary="article_tag_association", back_populates="article"
    )


class Author(db.Model):
    __tablename__ = "authors"

    id = db.Column(db.Integer, primary_key=True)
    users_id = db.Column(db.Integer, ForeignKey("users.id"), nullable=False)

    user = relationship("User", back_populates="author")
    article = relationship("Article", back_populates="author")


class Tag(db.Model):
    __tablename__ = "tags"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    article = relationship(
        "Article", secondary="article_tag_association", back_populates="tag"
    )


article_tag_associations_table = Table(
    "article_tag_association",
    db.metadata,
    db.Column("article_id", db.Integer, ForeignKey("articles.id"), nullable=False),
    db.Column("tag_id", db.Integer, ForeignKey("tags.id"), nullable=False),
)
