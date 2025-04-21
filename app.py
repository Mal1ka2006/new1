from flask import Flask, render_template, request, redirect, url_for, session, flash
import json, os
from functools import wraps

app = Flask(__name__)
app.secret_key = 'secret_key_here'

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