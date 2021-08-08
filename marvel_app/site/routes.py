from marvel_app.models import Character, db
from marvel_app.forms import CreateCharacter
from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user

# Creating blueprint for site routes
site = Blueprint('site', __name__, template_folder='site_templates')

@site.route('/')
def home():
    return render_template('index.html')

@site.route('/profile')
@login_required
def profile():
    owner = current_user.token
    characters = Character.query.filter_by(user_token = owner).all()
    return render_template('profile.html', characters = characters)

@site.route('/create', methods = ['GET', 'POST'])
@login_required
def create():
    form  = CreateCharacter()
    if request.method == 'POST' and form.validate_on_submit():
        name = form.name.data
        description = form.description.data
        movies = form.movies.data
        events = form.events.data
        series = form.series.data
        powers = form.powers.data
        snapped = form.snapped.data
        user_token = current_user.token
        character = Character(name, description, movies, events, series, powers, snapped, user_token)
        db.session.add(character)
        db.session.commit()
        return redirect(url_for('site.profile'))
    return render_template('create.html', form = form)