from flask import Blueprint, render_template
from flask_login import login_required, current_user
from sqlalchemy import select
from .model import Campain, UsersCampain
from . import db

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("home.html", user=current_user)

@views.route('/prowadzisz')
def MG_campains():
    data = Campain.query.filter_by(game_master=current_user.id)
    return render_template('MG_campains.html', user=current_user, campains=data)

@views.route('/grasz')
def playing_campains():
    user = current_user
    campains = db.session.query(Campain).filter(Campain.id == UsersCampain.campain_id).filter(user.id == UsersCampain.user_id).all()
    return render_template('playing_campains.html', user=current_user, campains=campains)

@views.route('/kampania/<id>')
def campain(id):
    data = db.session.query(Campain).filter(Campain.id == id).one()
    return render_template('campain.html', user=current_user, campain=data )

@views.route('/kontakt')
def contact():
    return render_template('contact.html', user=current_user)