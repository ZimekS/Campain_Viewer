from flask import Blueprint, render_template
from flask_login import login_required, current_user

campains = Blueprint('campains', __name__)

@campains.route('/dodaj_kampanie')
def add_campain():
    return render_template('add_campain.html', user=current_user)

@campains.route('/edytuj_kampanie')
def edit_campain():
    return render_template('edit_campain.html', user=current_user)