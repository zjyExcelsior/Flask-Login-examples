from .. import app
from flask import render_template, redirect, url_for, flash, request, abort
from ..models import User
from ..forms import LoginForm, RegistrationForm
from flask_login import login_user, login_required, logout_user
from .. import db

@app.route('/')
@login_required
def index():
    return render_template('index.html')


@app.route('/login/', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter(User.email == form.email.data).first()
        if user and user.password == form.password.data:
            # login...
            login_user(user, form.remember_me.data)
            # using next when you use @login_required
            next = request.args.get('next') # you can verify the next
            return redirect(next or url_for('index'))
        flash('Invalid username or password.')
    return render_template('login.html', form=form)


@app.route('/logout/')
@login_required
def logout():
    # logout...
    logout_user()
    return redirect(url_for('index'))

@app.route('/signup/', methods=['GET', 'POST'])
def signup():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email=form.email.data, 
                    username=form.username.data,
                    password=form.password.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('signup.html', form=form)
