from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect
from flask_admin import Admin
from blog.admin.views import CustomAdminIndexView
from flask_combo_jsonapi import Api


# def create_api_spec_plugin(app):
#     api_cpec_plugin = ApiSpecPlugin(
#         app=app,
#         tags={
#             "Tags": "Tags API",
#         },
#     )
#     return api_cpec_plugin


login_manager = LoginManager()
db = SQLAlchemy()
migrate = Migrate()
csrf = CSRFProtect()
admin = Admin(
    name="Blog Admin Panel",
    template_mode="bootstrap4",
    index_view=CustomAdminIndexView(),
)
api = Api()
