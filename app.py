from flask import Flask, render_template, redirect, flash, Response, session, url_for
from flask_compress import Compress
from flask_assets import Environment, Bundle
from database import connect_db, db
from forms import ContactForm, LoginForm, ProjectForm, SetPasswordForm
from models import Admin, Contact, get_column_names, Projects
from info import services, page_information, gallery_and_alt, before_afters
from dotenv import load_dotenv
import os
from flask_login import LoginManager

load_dotenv()
SENDGRID_API_KEY = os.getenv("SENDGRID_API_KEY")
SECRET_KEY = os.environ.get("SECRET_KEY", "default-secret-key")
DATABASE_URI = os.environ.get("DATABASE_URI")
SENDGRID_API_KEY = os.getenv("SENDGRID_API_KEY")

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI #'postgresql:///jpm'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = SECRET_KEY

Compress(app)
assets = Environment(app)
assets.auto_build = True  # Automatically build bundles on app startup
assets.debug = False      # Use production mode (minify output)


css = Bundle('about_us.css', 'contact_us.css', 'gallery.css', 'global.css', 'home.css', filters='cssmin', output='dist/css/styles.min.css')
js = Bundle('app.js', 'gallery.js', filters='jsmin', output='dist/scripts.min.js')
assets.register('css_all', css)
assets.register('js_all', js)


connect_db(app)

@app.context_processor #makes info global across all pages
def inject_services():
    return dict(services=services, page_information = page_information)

@app.route('/', methods=['GET', 'POST'])
def home():
    form = ContactForm()
    
    if form.validate_on_submit():
        if Contact.create_contact(form, complete=False):
            flash("Your form has been submitted. We try to get back to you the same day, expect a phone call or email from us.", "success")
            return redirect('/thank-you')
        else:
            flash('An error occurred while processing the form.')

    if form.errors:  # Check if there are validation errors
        flash("There was an error with your submission. Please fill out required fields", "danger")
        return redirect(url_for('home')  + '#Form-container')

    # Render the home page with the form and any error messages
    return render_template('home.jinja', form=form, active_page='home')

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
    form = ContactForm()
    if form.validate_on_submit():
        if Contact.create_contact(form, complete=True):
            flash("Your form has been submitted. We try to get back to you the same day, expect a phone call or email from us.", "success")
            return redirect('/thank-you')
        else:
            flash('An error occurred while processing the form.', 'danger')
    if form.errors:  # Check if there are validation errors
        flash("There was an error with your submission. Please fill out required fields", "danger")
        return render_template('contact_us.jinja', active_page='contact_us', form=form) 

    return render_template('contact_us.jinja', active_page = 'contact_us', form = form)

@app.route('/thank-you')
def thank_you():
    return render_template('thank_you.jinja',active_page = 'thank_you')

@app.route('/gallery', methods = ['GET', 'POST'])
def gallery():
    form = ContactForm()
    
    if form.validate_on_submit():
        if Contact.create_contact(form, complete=False):
            flash("Your form has been submitted. We try to get back to you the same day, expect a phone call or email from us.", "success")
            return redirect('/thank-you')
        else:
            flash('An error occurred while processing the form.')

    if form.errors:  # Check if there are validation errors
        flash("There was an error with your submission. Please fill out required fields", "danger")
        return redirect(url_for('gallery')  + '#Form-container')
    
    return render_template('gallery.jinja', active_page = 'gallery', gallery_and_alt = gallery_and_alt, before_afters = before_afters, form = form)



# Initialize Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'admin'  # type: ignore # Redirect to 'admin' login route for unauthenticated users
login_manager.login_message = 'Please log in as an admin to access this page.'
login_manager.login_message_category = 'danger'

@login_manager.user_loader
def load_user(admin_id):
    return Admin.query.get(int(admin_id))

from flask_login import login_user, login_required, logout_user, current_user

### beginning admin routes ###
@app.route('/admin', methods = ['GET', 'POST'])
def admin():
    form = LoginForm()

    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data

        admin = Admin.authenticate_admin(username = username, password = password)

        if admin:
            login_user(admin)
            flash('You are successfully logged in', 'success')
            return redirect(url_for('admin_dashboard'))
        else:
            flash('Incorrect password/username', 'danger')

    return render_template('admin/login.jinja', form = form, active_page = 'admin')


@app.route('/admin/dashboard', methods = ['GET','POST'])
@login_required
def admin_dashboard():
    admin = current_user

    contacts = Contact.query.all()
    contact_table_headers = get_column_names(Contact)
    projects = Projects.query.all()

    

    return render_template('admin/dashboard.jinja', active_page = 'admin-dashboard', admin = admin, contacts = contacts, table_headers = contact_table_headers, projects = projects)

@app.route('/admin/set-password', methods=['GET', 'POST'])
@login_required
def admin_set_password():
    """
    Allow the logged-in admin to update their password.
    """
    form = SetPasswordForm()
    if form.validate_on_submit():
        new_password = form.new_password.data

        try:
            current_user.set_password(new_password)
            db.session.commit()
            flash('Password successfully updated.', 'success')
            return redirect(url_for('admin_dashboard'))
        except Exception as e:
            db.session.rollback()
            flash(f'An error occurred: {str(e)}', 'danger')

    return render_template('admin/set_password.jinja', form=form, active_page='admin_set_password')



@app.route('/admin/add-contact', methods=['GET', 'POST'])
@login_required
def add_contact():
    form = ContactForm()
    if form.validate_on_submit():
        # Create a new Contact instance
        new_contact = Contact(
            name=form.name.data,phone=form.phone.data,email=form.email.data,address=form.address.data,service_type=form.service_type.data,message=form.message.data # type: ignore
        )

        # Save the new contact to the database
        db.session.add(new_contact)
        db.session.commit()

        flash('New contact added successfully!', 'success')
        return redirect(url_for('admin_dashboard'))

    return render_template('admin/contacts/add_contact.jinja', form=form)



@app.route('/admin/edit-contact/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_contact(id):
    contact = Contact.query.get_or_404(id)

    # Prepopulate the form with the contact's existing data
    form = ContactForm(obj=contact)

    if form.validate_on_submit():
        # Update contact with form data
        contact.name = form.name.data
        contact.email = form.email.data
        contact.address = form.address.data
        contact.service_type = form.service_type.data
        contact.message = form.message.data
        contact.phone = form.phone.data

        # Save changes to the database
        db.session.commit()
        flash('Contact updated successfully!', 'success')
        return redirect(url_for('admin_dashboard'))

    return render_template('admin/contacts/edit_contact.jinja', form=form)


@app.route('/admin/delete-contact/<int:id>', methods = ['POST'])
@login_required
def delete_contact(id):

    contact = Contact.query.get_or_404(id)
    db.session.delete(contact)
    db.session.commit()
    flash('Contact succesfully removed', 'success')
    return redirect(url_for('admin_dashboard'))

@app.route('/admin/delete-all-contacts', methods=['POST'])
@login_required
def delete_all_contacts():

    # Delete all contacts
    Contact.query.delete()
    db.session.commit()

    # Redirect with a success message
    flash('All contacts have been deleted.', 'success')
    return redirect(url_for('admin_dashboard'))


@app.route('/admin/add-project', methods=['GET', 'POST'])
@login_required
def add_project():


    form = ProjectForm()
    if form.validate_on_submit():
        # Create a new project
        new_project = Projects(
            type_of_work=form.type_of_work.data, # type: ignore
            service_id=form.service_id.data # type: ignore
        )
        db.session.add(new_project)
        db.session.commit()
        flash('New project added successfully!', 'success')
        return redirect(url_for('admin_dashboard'))

    return render_template('admin/projects/add_project.jinja', form=form, title='Add Project')


@app.route('/admin/edit-project/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_project(id):


    project = Projects.query.get_or_404(id)
    form = ProjectForm(obj=project)

    if form.validate_on_submit():
        # Update the project with form data
        project.type_of_work = form.type_of_work.data
        project.service_id = form.service_id.data

        db.session.commit()
        flash('Project updated successfully!', 'success')
        return redirect(url_for('admin_dashboard'))

    return render_template('admin/projects/edit_project.jinja', form=form, title='Edit Project', project=project)


@app.route('/admin/delete-project/<int:id>', methods=['POST'])
@login_required
def delete_project(id):



    project = Projects.query.get_or_404(id)
    db.session.delete(project)
    db.session.commit()
    flash('Project deleted successfully!', 'success')
    return redirect(url_for('admin_dashboard'))


@app.route('/logout', methods = ['GET', 'POST'])
@login_required
def logout():
    logout_user()
    flash('You have been logged out.', 'success')
    return redirect(url_for('admin'))

### end admin routes ###


#sitemap, robots.txt, and 404 routes
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
Disallow: /admin/dashboard
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

