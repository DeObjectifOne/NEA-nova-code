from flask import Blueprint, render_template

pages = Blueprint('pages', __name__)

#route used for the page
@pages.route('/')
def home():
    return render_template("home.html")