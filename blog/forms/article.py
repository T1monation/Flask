from flask_wtf import FlaskForm
from wtforms import StringField, validators, SubmitField, TextAreaField


class ArticleCreateForm(FlaskForm):
    title = StringField("Title", [validators.DataRequired()])
    text = TextAreaField("Text", [validators.DataRequired()])
    submit = SubmitField("Create")
