from flask import Blueprint, render_template, request, flash, redirect, url_for, current_app
from werkzeug.security import generate_password_hash, check_password_hash
from .model import User
from .token import generate_confirmation_token, confirm_account
from flask_mail import Message
from . import db, mail
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        
        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Zalogowano', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Nieprawidłowe hasło', category='error')
        else:
            flash('Użytkowanik nie istnieje', category='error')

    return render_template("login.html", user=current_user)

@auth.route('/wylogowanie')
@login_required
def logout():
    logout_user()
    flash('Wylogowano', category='success')
    return redirect(url_for('views.home'))

@auth.route('/rejestracja', methods=['GET', 'POST'])
def signUp():
    if request.method == 'POST':
        email = request.form.get('email')
        name = request.form.get('name')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        user = User.query.filter_by(email=email).first()
        
        if user:
            flash('Już istnieje taki użytkownik', category='error')
        elif len(name) <= 2:
            flash('Twoja nazwa musi mieć conajmniej 3 znaki', category='error')
        elif password1 != password2:
            flash('Hasła się nie zgadzają', category='error')
        elif len(password1) < 8:
            flash('Hasło musi mieć conajmniej 8 znaków', category='error')
        else:
            if email == current_app.config['FLASKY_ADMIN']:
                new_user = User(email=email, name=name, password=generate_password_hash(password1, method='sha256'))
                new_user.confirmed = True
                new_user.role = 'Admin'
                db.session.add(new_user)
                db.session.commit()
                login_user(new_user, remember=True)
                return redirect(url_for('views.home'))
            else:
                new_user = User(email=email, name=name, password=generate_password_hash(password1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            token = generate_confirmation_token(new_user.email)
            msg = Message('Confirm your account.', sender=current_app.config['MAIL_USERNAME'], recipients= [new_user.email])
            msg.body = f"Drogi {new_user.name},\nWitamy w Campain Viewer!\nAby potwierdzić swoje konto, kliknij ten link:\n{url_for('auth.confirm_email', token=token, _external=True)}\nZ poważaniem,\nZespół Campain Viewer\nUwaga: Nie odpowiadaj na tę wiadomość."
            mail.send(msg)
            login_user(new_user, remember=True)
            flash('Wysłaliśmy link potwierdzający konto na Twój adres email', category='success')
            return redirect(url_for('views.home'))
            
    return render_template("signUp.html", user=current_user)

@auth.route('/confirm/<token>')
@login_required
def confirm_email(token):
    try:
        email = confirm_account(token)
    except:
        flash('Link potwierdzajacy wygasl', category='error')
    user = User.query.filter_by(email=email).first_or_404()
    if user.confirmed:
        flash('Konto zostalo już potwierdzone. Można się zalogować', category='success')
    else:
        user.confirmed = True
        db.session.add(user)
        db.session.commit()
        flash('Potwierdziłeś swoje konto, Dzięki!', category='success')
    return redirect(url_for('views.home'))