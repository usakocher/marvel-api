from flask import Blueprint, render_template, request, flash, redirect, url_for
from marvel_app.forms import UserSignUpForm, UserLoginForm
from marvel_app.models import User, db, check_password_hash
from flask_login import login_user, logout_user, login_required

# Creating blueprint for authorization routes
auth = Blueprint('auth', __name__, template_folder='auth_templates')

@auth.route('/signup', methods = ['GET', 'POST'])
def signup():
    form = UserSignUpForm()
    if request.method == 'POST' and form.validate_on_submit():
        first_name = form.first_name.data
        last_name = form.last_name.data
        username = form.username.data
        email = form.email.data
        password = form.password.data
        confirm = form.confirm.data
        print([first_name,last_name,username,email,password,confirm])
        new_user = User(first_name, last_name, username, email, password)
        db.session.add(new_user)
        db.session.commit()
        flash(f'You have successfully created a user account {username}', 'user_created')
        return redirect(url_for('auth.signin'))
    return render_template('signup.html', form = form)

@auth.route('/signin', methods = ['GET', 'POST'])
def signin():
    form = UserLoginForm()
    if request.method == 'POST' and form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        print([username, password])
        logged_user = User.query.filter(User.username == username).first()
        if logged_user and check_password_hash(logged_user.password, password):
            login_user(logged_user)
            flash(f'Successfully logged in as: {username}', 'auth_success')
            return redirect(url_for('site.home'))
        else:
            flash('Email or password is incorrect, please try again', 'auth_failed')
            return redirect(url_for('auth.signin'))
    return render_template('signin.html', form = form)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash(f'Successfully logged out of account', 'logout_success')
    return redirect(url_for('auth.signin'))