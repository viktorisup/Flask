from flask import Blueprint, render_template


report = Blueprint('report', __name__, url_prefix='/reports', static_folder='../static')

REPORTS = [1,2,3,45]
@report.route('/')
def report_list():
    return render_template(
        'reports/list.html',
        reports=REPORTS,

    )