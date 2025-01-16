from os import cpu_count
from flask import Flask, render_template, redirect, flash, session
from database import connect_db, db
from forms import ContactForm, LoginForm
from models import Admin, Contact
from secret import SECRET_KEY, services, page_information

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///jpm'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = SECRET_KEY

connect_db(app)





@app.context_processor
def inject_services():
    return dict(services=services, page_information = page_information)

@app.route('/', methods = ['GET', 'POST'])
def home():
    quickForm = ContactForm()
    if quickForm.validate_on_submit():
        name = quickForm.name.data
        phone = quickForm.phone.data
        email = quickForm.email.data
        service_type = quickForm.service_type.data

        new_contact = Contact(name = name, phone = phone, email = email, service_type = service_type) # type: ignore
        db.session.add(new_contact)
        db.session.commit()

        flash("Your form has been submitted. We try to get back to you the same day, expect a phone call or email from us.", "success")
        return redirect('/')
    
    return render_template('home.jinja', form = quickForm, active_page='home')


















### service routes ###
@app.route('/asphalt')
def asphalt():

    return render_template('services/asphalt.jinja', active_page = 'asphalt', service = services.get('asphalt'))

@app.route('/concrete')
def concrete():

    return render_template('services/concrete.jinja', active_page = 'concrete', service = services.get('concrete'))

@app.route('/home-improvement')
def home_improvement():

    return render_template('services/home_improvement.jinja', active_page = 'home_improvement', service = services.get('home_improvement'))

@app.route('/masonry')
def masonry():

    return render_template('services/masonry.jinja', active_page = 'masonry', service = services.get('masonry'))

@app.route('/paver-sealing')
def paver_sealing():

    return render_template('services/paver_sealing.jinja', active_page = 'paver_sealing', service = services.get('paver_sealing'))

@app.route('/pressure-washing')
def pressure_washing():

    return render_template('services/pressure_washing.jinja',active_page = 'pressure_washing', service = services.get('pressure_washing'))

### end service routes ###

##misc routes###

@app.route('/about-us')
def about_us():

    return render_template('about_us.jinja', active_page = 'about_us')

@app.route('/financing')
def financing():

    return render_template('financing.jinja', active_page = 'financing')

@app.route('/contact-us', methods = ['GET', 'POST'])
def contact_us():

    fullForm = ContactForm()
    if fullForm.validate_on_submit():
        name = fullForm.name.data
        phone = fullForm.phone.data
        email = fullForm.email.data
        service_type = fullForm.service_type.data
        address = fullForm.address.data
        message = fullForm.message.data

        new_contact = Contact(name = name, phone = phone, email = email, service_type = service_type, address = address, message = message) # type: ignore
        db.session.add(new_contact)
        db.session.commit()

        flash("Your form has been submitted. We try to get back to you the same day, expect a phone call or email from us.", "success")
        return redirect('/')

    return render_template('contact_us.jinja', active_page = 'contact_us', form = fullForm)

@app.route('/gallery')
def gallery():
    return render_template('gallery.jinja', active_page = 'gallery')

@app.route('/admin', methods = ['GET', 'POST'])
def admin():
    form = LoginForm()

    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data

        admin = Admin.authenticate_admin(username = username, password = password)

        if admin:
            flash('You are successfully logged in', 'success')
            session['admin-username'] = admin.username
            return redirect('/admin-dashboard')
        else:
            flash('You do not have access', 'danger')

    return render_template('admin.jinja', form = form, active_page = 'admin')

@app.route('/admin-dashboard', methods = ['GET','POST'])
def admin_dashboard():
    if 'admin-username' not in session:
        flash('You are not allowed to view this page' , 'danger')
        return redirect('/')
    
    admin = Admin.query.filter_by(username= session['admin-username']).first()
    contacts = Contact.query.all()

    return render_template('admin_dashboard.jinja', active_page = 'admin-dashboard', admin = admin, contacts = contacts)

@app.route('/admin/set-password', methods = ['GET', 'POST'])
def admin_set_password():
    if 'admin-username' not in session:
        flash('You are not allowed to view this page' , 'danger')
        return redirect('/')

    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        new_password = form.password.data

        admin = Admin.query.filter_by(username = username).first()
        if admin:
            admin.set_password(new_password)
            db.session.commit()
            flash('Password successfully updated' , 'success')
            return redirect('/admin-dashboard')
        else:
            flash('An error occurred. Admin not found.', 'danger')

        return redirect('/admin_dashboard')
    
    return render_template('admin_set_password.jinja', form = form, active_page = 'admin_set_password')


@app.route('/logout', methods = ['GET', 'POST'])
def logout():
    if 'admin-username' in session:
        session.pop('admin-username')
        flash('You have successfully been logged out' , 'info')
    else:
        flash('You are not logged in' , 'danger')
        return redirect('/admin')
    return redirect('/')

### end misc routes ###
