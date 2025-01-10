from flask import Flask, render_template
from database import connect_db
from secret import SECRET_KEY

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///jpm'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = SECRET_KEY

connect_db(app)

@app.route('/')
def home():
    return render_template('home.jinja')


















### service routes ###
@app.route('/')
def asphalt():
    return render_template('asphalt.jinja')

@app.route('/concrete')
def concrete():
    return render_template('concrete.jinja')

@app.route('/home-improvement')
def home_improvement():
    return render_template('home_improvement.jinja')

@app.route('/masonry')
def masonry():
    return render_template('masonry.jinja')

@app.route('/paver-sealing')
def paver_sealing():
    return render_template('paver_sealing.jinja')

@app.route('/pressure-washing')
def pressure_washing():
    return render_template('pressure_washing.jinja')

### end service routes ###

##misc routes###

@app.route('/about')
def about_us():
    return render_template('about_us.jinja')

@app.route('/financing')
def financing():
    return render_template('financing.jinja')

@app.route('/contact')
def contact_us():
    return render_template('contact_us.jinja')

@app.route('/gallery')
def gallery():
    return render_template('gallery.jinja')

### end misc routes ###
