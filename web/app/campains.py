from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user
from .model import Campain, User, UsersCampain
from . import db
import os
from werkzeug.utils import secure_filename

campains = Blueprint('campains', __name__)
UPLOAD_FOLDER  = "/usr/src/campViewer/app/static"
#ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

@campains.route('/dodaj_kampanie', methods=['GET', 'POST'])
def add_campain():
    if request.method == 'POST':
        userId = current_user.id
        name = request.form.get('name')
        description = request.form.get('description')
        file = request.form.get('file')
        path_to_file = upload_file(file, None)
        new_campain = Campain(name=name, description=description, img=path_to_file, session_number=0, game_master=userId)
        db.session.add(new_campain)
        db.session.commit()
        flash('Dodałeś swoją kampanię', category='success')
    return render_template('add_campain.html', user=current_user)

@campains.route('/edytuj_kampanie/<id>', methods=['GET', 'POST'])
def edit_campain(id):
    campain = db.session.query(Campain).filter(Campain.id == id).first()
    if request.method == 'GET':
        return render_template('edit_campain.html', campain=campain, user=current_user)
    elif request.method == 'POST':
        if request.form.get('player'):
            player = request.form.get('player')
            new_player = db.session.query(User).filter(User.name == player).first()
            if new_player:
                new_connection = UsersCampain(user_id=new_player.id, campain_id=id)
                db.session.add(new_connection)
                db.session.commit()
                message = "Dodano gracza " + str(new_player.name)
                flash(message, category='success')
                return render_template('edit_campain.html', campain=campain, user=current_user)
            else:
                flash('Nie ma takiego gracza', category='error')
                return render_template('edit_campain.html', campain=campain, user=current_user)
                
        else:
            name = request.form.get('name')
            description = request.form.get('description')
            file = request.form.get('file')
            path_to_file = upload_file(file, campain)
            campain = db.session.query(Campain).filter(Campain.id == id).first()
            setattr(campain, 'name', name)
            setattr(campain, 'description', description)
            setattr(campain, 'img', path_to_file)
            db.session.commit()
            flash('Zaaktualizowano kampanię', category='success')
            redirect_path = 'views.kampania.' + str(id)
            return render_template('edit_campain.html', campain=campain, user=current_user)
    
    return render_template('edit_campain.html', user=current_user)

def upload_file(file, campain):
    if request.method == 'POST':
        file = request.files['file']
        if file:
            filename = secure_filename(file.filename)
            file.save(os.path.join(UPLOAD_FOLDER, filename))
            return str(filename)
        else:
            if campain == None:
                return "Brak"
            else:
                return campain.img