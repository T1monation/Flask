from flask_wtf import FlaskForm
from wtforms import StringField, validators, PasswordField, SubmitField


class UserRegisterForm(FlaskForm):
    first_name = StringField("First name")
    last_name = StringField("Last name")
    email = StringField("E-mail", [validators.DataRequired(), validators.Email()])
    password = PasswordField(
        "Password",
        [
            validators.DataRequired(),
            validators.EqualTo(
                "confrim_password", message="Field must be equal to password"
            ),
        ],
    )
    confrim_password = PasswordField("Confrim password", [validators.DataRequired()])
    submit = SubmitField("Register")


class UserLoginForm(FlaskForm):
    email = StringField(
        "E-mail",
        [
            validators.DataRequired(),
            validators.Email(),
        ],
    )
    password = PasswordField("Password", [validators.DataRequired()])
    submit = SubmitField("Login")
