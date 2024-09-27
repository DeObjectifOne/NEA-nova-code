from flask import Blueprint

#creates a blueprint called forms
#this can be imported elsewhere
forms = Blueprint('forms', __name__)

#route used for the login page
@forms.route('/login')
def login():
    return "<p>login</p>"

#route used for the logout function
@forms.route('/logout')
def logout():
    return "<p>logout</p>"

#route used for the sign-up page
@forms.route('/sign-up')
def sign_up():
    return "<p>sign-up</p>"


