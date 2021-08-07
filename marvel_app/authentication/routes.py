from flask import Blueprint, render_template

# Creating blueprint for authorization routes
auth = Blueprint('auth', __name__, template_folder='auth_templates')

@auth.route('/signup')
def signup():
    return render_template('signup.html')

@auth.route('/signin')
def signin():
    return render_template('signin.html')