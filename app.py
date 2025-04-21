from flask import Flask, render_template, request, redirect, url_for, session, flash
import json, os
from functools import wraps

app = Flask(__name__)
app.secret_key = 'secret_key_here'


def load_json(filepath, default={}):
    if not os.path.exists(filepath):
        with open(filepath, 'w') as f:
            json.dump(default, f)
    with open(filepath, 'r') as f:
        return json.load(f)
def prosto():
    q=0
    return q

def save_json(filepath, data):
    with open(filepath, 'w') as f:
        json.dump(data, f, indent=4)
=======
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user' not in session:
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function



@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['user'] = request.form['username']
        return redirect(url_for('menu'))
    return render_template('login.html')
=======
@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('login'))
=======









@app.route('/menu')
@login_required
def menu():
    data = load_json('data/food_data.json')
    return render_template('menu.html', data=data)

