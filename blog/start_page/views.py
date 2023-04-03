from flask import Blueprint
from flask import render_template, url_for
from werkzeug.exceptions import NotFound
from werkzeug.security import generate_password_hash
from flask import redirect
from blog.app import login_manager
from flask_login import login_required, current_user, login_user
from blog.forms.user import UserRegisterForm
from flask import request
from blog.models import User
from blog.extensions import db
from psycopg2 import IntegrityError
import requests
from blog.config import API_URL


start_page = Blueprint("start_page", __name__, static_folder="../static",
                       )


@start_page.route("/")
def index():
    return render_template("start_page/start.html")
