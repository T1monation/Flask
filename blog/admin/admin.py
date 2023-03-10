from flask import Blueprint
from flask import render_template
from flask_login import login_required, current_user
from blog.models import User


admin = Blueprint("admin", __name__, static_folder="../static", url_prefix="/admin")


@admin.route("/")
@login_required
def admin_view():
    if current_user.is_admin:
        return render_template("admin/admin.html")
    else:
        pass
