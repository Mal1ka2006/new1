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