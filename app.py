from flask import Flask, render_template, redirect, flash
from database import connect_db, db
from forms import ContactForm
from models import Contact
from secret import SECRET_KEY

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///jpm'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = SECRET_KEY

connect_db(app)

@app.route('/', methods = ['GET', 'POST'])
def home():
    meta_description = "JPM and Sons offers general contracting services throughout Long Island. Specializing in masonry, concrete, asphalt paving, paver sealing, pressure washing, and home improvement. Get a free estimate today!"

    form = ContactForm()
    if form.validate_on_submit():
        name = form.name.data
        phone = form.phone.data
        email = form.email.data
        address = form.address.data
        service_type = form.service_type.data
        message = form.message.data

        new_contact = Contact(name = name, phone = phone, email = email, address = address, service_type = service_type, message = message) # type: ignore
        db.session.add(new_contact)
        db.session.commit()

        flash("Your form has been submitted. We try to get back to you the same day, keep an eye on your email.", "success")
        return redirect('/')
    
    return render_template('home.jinja', form = form, active_page='home', meta_description = meta_description)


















### service routes ###
@app.route('/asphalt')
def asphalt():
    meta_description = ""

    return render_template('services/asphalt.jinja', active_page = asphalt, meta_description = meta_description)

@app.route('/concrete')
def concrete():
    meta_description = ""

    return render_template('services/concrete.jinja', active_page = concrete, meta_description = meta_description)

@app.route('/home-improvement')
def home_improvement():
    meta_description = ""

    return render_template('services/home_improvement.jinja', active_page = home_improvement, meta_description = meta_description)

@app.route('/masonry')
def masonry():
    meta_description = ""

    return render_template('services/masonry.jinja', active_page = masonry, meta_description = meta_description)

@app.route('/paver-sealing')
def paver_sealing():
    meta_description = ""

    return render_template('services/paver_sealing.jinja', active_page = paver_sealing, meta_description = meta_description)

@app.route('/pressure-washing')
def pressure_washing():
    meta_description = ""

    return render_template('services/pressure_washing.jinja',active_page = pressure_washing, meta_description = meta_description)

### end service routes ###

##misc routes###

@app.route('/about-us')
def about_us():
    meta_description = ""

    return render_template('about_us.jinja', active_page = about_us, meta_description = meta_description)

@app.route('/financing')
def financing():
    meta_description = ""

    return render_template('financing.jinja', active_page = financing, meta_description = meta_description)

@app.route('/contact-us')
def contact_us():
    meta_description = ""

    return render_template('contact_us.jinja', active_page = contact_us, meta_description = meta_description)

@app.route('/gallery')
def gallery():
    meta_description = ""
    return render_template('gallery.jinja', active_page = gallery, meta_description = meta_description)

### end misc routes ###
