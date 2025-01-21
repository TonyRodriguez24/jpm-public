from flask import Flask, render_template, redirect, flash, Response, session, url_for
from flask_compress import Compress
from flask_assets import Environment, Bundle
from database import connect_db, db
from forms import ContactForm, LoginForm
from models import Admin, Contact
from secret import SECRET_KEY, services, page_information, gallery_and_alt, before_afters


app = Flask(__name__)
Compress(app)
assets = Environment(app)
assets.auto_build = True  # Automatically build bundles on app startup
assets.debug = False      # Use production mode (minify output)


css = Bundle(
    'about_us.css',
    'contact_us.css',
    'gallery.css',
    'global.css',
    'home.css',
    filters='cssmin',
    output='dist/css/styles.min.css'
    )

js = Bundle(
    'app.js',
    'gallery.js',
    filters='jsmin',
    output='dist/scripts.min.js'
)

assets.register('css_all', css)
assets.register('js_all', js)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///jpm'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = SECRET_KEY

connect_db(app)





@app.context_processor
def inject_services():
    return dict(services=services, page_information = page_information)







@app.route('/', methods=['GET', 'POST'])
def home():
    quickForm = ContactForm()
    
    if quickForm.validate_on_submit():
        # Process the form data
        name = quickForm.name.data
        phone = quickForm.phone.data
        email = quickForm.email.data
        service_type = quickForm.service_type.data

        # Create a new contact entry in the database
        new_contact = Contact(name=name, phone=phone, email=email, service_type=service_type)  # type: ignore
        db.session.add(new_contact)
        db.session.commit()

        # Flash success message
        flash("Your form has been submitted. We try to get back to you the same day. Expect a phone call or email from us.", "success")
        return redirect('/thank-you')
    
    if quickForm.errors:  # Check if there are validation errors
        flash("There was an error with your submission. Please make sure you have selected a service.", "danger")
        return redirect(url_for('home') + '#Form-container')

    
    # Render the home page with the form and any error messages
    return render_template('home.jinja', form=quickForm, active_page='home')




















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
        referral = fullForm.referral.data

        new_contact = Contact(name = name, phone = phone, email = email, service_type = service_type, address = address, referral =referral, message = message) # type: ignore
        db.session.add(new_contact)
        db.session.commit()

        flash("Your form has been submitted. We try to get back to you the same day, expect a phone call or email from us.", "success")
        return redirect('/thank-you')
    
    if fullForm.errors:  # Check if there are validation errors
        flash("There was an error with your submission. Please fill out required fields", "danger")
        return redirect('/contact-us')

    return render_template('contact_us.jinja', active_page = 'contact_us', form = fullForm)



@app.route('/thank-you')
def thank_you():
    return render_template('thank_you.jinja',active_page = 'thank_you')

@app.route('/gallery', methods = ['GET', 'POST'])
def gallery():
    quickForm = ContactForm()
    
    if quickForm.validate_on_submit():
        # Process the form data
        name = quickForm.name.data
        phone = quickForm.phone.data
        email = quickForm.email.data
        service_type = quickForm.service_type.data

        # Create a new contact entry in the database
        new_contact = Contact(name=name, phone=phone, email=email, service_type=service_type)  # type: ignore
        db.session.add(new_contact)
        db.session.commit()

        # Flash success message
        flash("Your form has been submitted. We try to get back to you the same day. Expect a phone call or email from us.", "success")
        return redirect('/thank-you')
    
    if quickForm.errors:  # Check if there are validation errors
        flash("There was an error with your submission. Please make sure you have selected a service.", "danger")
        return redirect(url_for('gallery')  + '#Form-container')
    
    return render_template('gallery.jinja', active_page = 'gallery', gallery_and_alt = gallery_and_alt, before_afters = before_afters, form = quickForm)

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
            flash('Incorrect password/username', 'danger')

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


@app.route('/sitemap.xml', methods=['GET'])
def sitemap():
    from flask import Response
    import datetime

    # Correct endpoint names for excluded routes
    excluded_routes = ['admin', 'admin_dashboard', 'admin_set_password', 'logout', 'robots_txt', 'sitemap']
    sitemap_xml = ['<?xml version="1.0" encoding="utf-8"?>']
    sitemap_xml.append('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">')

    try:
        # Generate sitemap entries
        for rule in app.url_map.iter_rules():
            # Only include GET methods and routes without arguments
            if rule.methods and "GET" in rule.methods and not rule.arguments:
                if rule.endpoint not in excluded_routes:
                    try:
                        url = url_for(rule.endpoint, _external=True)
                        last_modified = datetime.datetime.now().date()
                        sitemap_xml.append(
                            f'<url><loc>{url}</loc><lastmod>{last_modified}</lastmod></url>'
                        )
                    except Exception as e:
                        print(f"Error adding URL for rule {rule}: {e}")

        sitemap_xml.append('</urlset>')
        sitemap_content = '\n'.join(sitemap_xml)

        # Return the generated sitemap
        return Response(sitemap_content, mimetype='application/xml')

    except Exception as e:
        print(f"Error generating sitemap: {e}")
        return Response("Error generating sitemap", status=500, mimetype='text/plain')

@app.route('/robots.txt')
def robots_txt():
    response = """User-agent: *
Disallow: /admin
Disallow: /admin-dashboard
Disallow: /admin/set-password
Disallow: /logout
Allow: /

Sitemap: https://jpmandsons.com/sitemap.xml
"""
    return Response(response, mimetype='text/plain')

@app.errorhandler(404)
def page_not_found(e):
    # Render the 404 template with a 404 status code
    return render_template('404.jinja'), 404

