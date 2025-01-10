from flask import Flask, render_template
from database import db, connect_db
import os

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'postgresql:///playlist_app')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['WTF_CSRF_ENABLED'] = True  # Ensure CSRF is enabled
app.config['SECRET_KEY'] = 'asdfasdf'

connect_db(app)

@app.route('/')
def home():
    return render_template('home.jinja')

