from flask import Blueprint, render_template

bp = Blueprint('home', __name__)


@bp.route('/', methods=['GET'])
def index():
    context_data = {
        "title": "NSH Toolbox"
    }
    return render_template("home.html", **context_data)


