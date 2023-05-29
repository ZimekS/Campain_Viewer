from flask import Blueprint, render_template, request, flash
from flask_login import login_required, current_user
from .model import Campain
from . import db

campains = Blueprint('campains', __name__)

@campains.route('/dodaj_kampanie', methods=['GET', 'POST'])
def add_campain():
    if request.method == 'POST':
        userId = current_user.id
        name = request.form.get('name')
        description = request.form.get('description')
        img = request.form.get('img')
        new_campain = Campain(name=name, description=description, game_master=userId)
        db.session.add(new_campain)
        db.session.commit()
        flash('Dodałeś swoją kampanię', category='success')
    return render_template('add_campain.html', user=current_user)

@campains.route('/edytuj_kampanie')
def edit_campain():
    return render_template('edit_campain.html', user=current_user)