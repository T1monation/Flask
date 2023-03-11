from flask import Flask
from blog import commands
from blog.extensions import db, login_manager, migrate, csrf
from blog.models import User


def create_app() -> Flask:
    app = Flask(__name__)
    # app.config["SECRET_KEY"] = "lc+lb_^62*cfxf!5r32kd-obejem8rsejw=!l!v+tvfk00ivux"
    # app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://flask:123456@localhost/blog"
    # app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config.from_object("blog.config")

    register_extensions(app)
    register_blueprints(app)
    register_commands(app)
    return app


def register_extensions(app):
    db.init_app(app)
    migrate.init_app(app, db, compare_type=True)
    csrf.init_app(app)

    login_manager.login_view = "auth.login"
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))


def register_blueprints(app: Flask):
    from blog.report.views import report
    from blog.user.views import user
    from blog.article.views import article
    from blog.auth.views import auth
    from blog.admin.admin import admin

    app.register_blueprint(user)
    app.register_blueprint(report)
    app.register_blueprint(article)
    app.register_blueprint(auth)
    app.register_blueprint(admin)


def register_commands(app: Flask):
    app.cli.add_command(commands.create_fake_data)
    app.cli.add_command(commands.create_admin)
