from flask import Flask, render_template, redirect, flash
from database import connect_db
from forms import ContactForm
from secret import SECRET_KEY

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///jpm'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = SECRET_KEY

connect_db(app)

@app.route('/')
def home():
    form = ContactForm()
    if form.validate_on_submit():
        name = form.name.data
        phone = form.phone.data
        email = form.email.data
        address = form.address.data
        service_type = form.service_type.data
        message = form.message.data

        flash("Your form has been submitted", "success")
        return redirect('/thank-you')
    return render_template('home.jinja', form = form)


















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
