from flask import Blueprint
from flask import render_template


report = Blueprint("report", __name__, static_folder="../static", url_prefix="/reports")


@report.route("/")
def report_list():
    return render_template("reports/list.html", reports=[1, 2, 3, 4, 5])
