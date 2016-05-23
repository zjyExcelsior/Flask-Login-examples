# coding: utf-8
from flask import render_template, redirect, url_for, flash, request, abort
from flask import Blueprint
from ..forms import LoginForm, RegistrationForm
from flask_login import login_user, login_required, logout_user, current_user
from ..models import User
from .. import db

auth = Blueprint('auth', __name__)


@auth.route('/login/', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter(User.email == form.email.data).first()
        if user and user.password == form.password.data:
            # Keep the user info in the session using Flask-Login
            login_user(user, form.remember_me.data)

            # using next when you use @login_required
            next = request.args.get('next')  # you can verify the next
            return redirect(next or url_for('main.index'))
        flash('Invalid username or password.')
    return render_template('auth/login.html', form=form)


@auth.route('/logout/')
@login_required
def logout():
    # Remove the user information from the session
    logout_user()
    return redirect(url_for('main.index'))


@auth.route('/signup/', methods=['GET', 'POST'])
def signup():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email=form.email.data,
                    username=form.username.data,
                    password=form.password.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('.login'))
    return render_template('auth/signup.html', form=form)
