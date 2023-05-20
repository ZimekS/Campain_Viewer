from flask import Blueprint, render_template
from flask_login import login_required, current_user

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("home.html", user=current_user)

@views.route('/prowadzisz')
def MG_campains():
    return render_template('MG_campains.html', user=current_user)

@views.route('/grasz')
def playing_campains():
    return render_template('playing_campains.html', user=current_user)

@views.route('/dodaj_kampanie')
def add_campains():
    return render_template('add_campain.html', user=current_user)