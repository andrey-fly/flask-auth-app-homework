from flask import Blueprint, render_template, jsonify, request
from flask_login import login_required, current_user
from .models import Pizza
from . import db

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html', name=current_user.name)

@main.route('/pizza')
@login_required
def pizza():
    data = [{'id': p.id, 'name': p.name, 'price': p.price} for p in Pizza.query.all()]
    return jsonify(data)

@main.route('/addpizza', methods=['POST'])
@login_required
def add_pizza():
    name = request.form.get('name')
    price = request.form.get('price')

    new_pizza = Pizza(name=name, price=price)

    db.session.add(new_pizza)
    db.session.commit()
    return render_template('addpizza.html')

@main.route('/addpizza')
@login_required
def add_pizza_post():
    return render_template('addpizza.html')

