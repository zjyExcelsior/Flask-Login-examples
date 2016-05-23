# coding: utf-8
from flask import render_template, redirect, url_for, flash
from flask import Blueprint
from flask_login import current_user, login_required

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/admin/')
@login_required
def admin():
    if current_user.role_id != 1:
        flash('you don\'t have the permission')
        return redirect(url_for('.index'))
    return '<p>hello world</p>'