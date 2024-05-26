from flask import Blueprint, render_template, current_app

bp = Blueprint("pages", __name__)

@bp.route("/")
def home():
    # return "Hello, World!"
    # current_app.logger.info('age home was not found')
    return render_template("pages/home.html")

@bp.route("/about")
def about():
    # return "About!"
    return render_template("pages/about.html")
