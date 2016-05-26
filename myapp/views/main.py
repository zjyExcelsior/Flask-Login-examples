# coding: utf-8
from flask import render_template, redirect, url_for, flash
from flask import Blueprint
from flask_login import current_user, login_required
from ..utils.dbMethods import get_role_names
from flask import request, jsonify
import json

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


@main.route('/test_roles/')
def test_roles():
    return str(get_role_names())


@main.route('/get_ip/')
def get_ip():
    # 得到访问者的ip地址
    return jsonify({'ip': request.environ.get('REMOTE_ADDR', request.remote_addr)})
    # return request.environ.get('HTTP_X_REAL_IP', request.remote_addr)
