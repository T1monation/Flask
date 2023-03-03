from flask import Flask, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

from flask_login import LoginManager


db = SQLAlchemy()
login_manager = LoginManager()


def create_app() -> Flask:
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "lc+lb_^62*cfxf!5r32kd-obejem8rsejw=!l!v+tvfk00ivux"
    app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://flask:123456@localhost/blog"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)

    login_manager.login_view = "auth.login"
    login_manager.init_app(app)
    from .models import User

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    # @login_manager.unauthorized_handler
    # def unauthorized():
    #     return redirect(url_for("auth.login"))

    register_blueprints(app)
    return app


def register_blueprints(app: Flask):
    from blog.report.views import report
    from blog.user.views import user
    from blog.article.views import article
    from blog.auth.views import auth

    app.register_blueprint(user)
    app.register_blueprint(report)
    app.register_blueprint(article)
    app.register_blueprint(auth)
