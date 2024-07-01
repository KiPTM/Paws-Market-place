from flask import render_template, flash, redirect, url_for
from flask_login import current_user, login_user, logout_user, login_required
from app import db
from app.models import User, Product
from flask import Blueprint

bp = Blueprint('main', __name__)

@bp.route('/')
@bp.route('/index')
def index():
    products = Product.query.all()
    return render_template('index.html', title='Home', products=products)

@bp.route('/login', methods=['GET', 'POST'])
def login():
    # Implement login functionality
    pass

@bp.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.index'))
