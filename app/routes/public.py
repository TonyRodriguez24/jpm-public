from flask import Blueprint, current_app, flash, redirect, render_template, request, url_for
import requests
from markdown2 import markdown
from app.forms import ContactForm
from app.models import Blogs, Contact
from app.info import services, buttons, gallery_and_alt, before_afters

public = Blueprint('public', __name__)

@public.route('/', methods=['GET', 'POST'])
def home():
    """Rendering home template and handling (quick) form on home page"""
    #gets the reCAPTCHA token from the form submission


    form = ContactForm()
    
    if form.validate_on_submit():
        recaptcha_response = request.form.get('g-recaptcha-response')

        #verify the token with reCAPTCHA API
        verify_url = 'https://www.google.com/recaptcha/api/siteverify'
        payload = {'secret': current_app.config.get('RECAPTCHA_SECRET_KEY'), 'response': recaptcha_response, 'remoteip': request.remote_addr}
        current_app.logger.debug(f"reCAPTCHA payload: {{'secret': '*****', 'response': {payload['response']}, 'remoteip': {payload['remoteip']}}}")
        result = requests.post(verify_url, data = payload).json()

        if result.get('success'):
            if Contact.create_contact(form, complete=False):
                return redirect('/thank-you')
            else:
                flash('An error occurred while processing the form.', 'danger')
        else:
            flash("Invalid reCAPTCHA. Please try again.", "danger")
            return redirect(url_for('public.home') + '#ContactForm')


    #validation errors
    if form.errors:
        flash("There was an error with your submission. Please fill out required fields", "danger")
        return redirect(url_for('public.home')  + '#ContactForm')

    # Render the home page with the form and any error messages
    return render_template('public/home.jinja', form=form, active_page='home')

### service routes - setting active page, getting service from services object, getting buttons from buttons object ###
@public.route('/asphalt')
def asphalt():
    return render_template('public/services/asphalt.jinja', active_page = 'asphalt', service = services.get('asphalt'), buttons = buttons)
@public.route('/concrete')
def concrete():
    return render_template('public/services/concrete.jinja', active_page = 'concrete', service = services.get('concrete'), buttons = buttons)
@public.route('/home-improvement')
def home_improvement():
    return render_template('public/services/home_improvement.jinja', active_page = 'home_improvement', service = services.get('home_improvement'), buttons = buttons)
@public.route('/masonry')
def masonry():
    return render_template('public/services/masonry.jinja', active_page = 'masonry', service = services.get('masonry'), buttons = buttons)
@public.route('/paver-sealing')
def paver_sealing():
    return render_template('public/services/paver_sealing.jinja', active_page = 'paver_sealing', service = services.get('paver_sealing'), buttons = buttons)
@public.route('/pressure-washing')
def pressure_washing():
    return render_template('public/services/pressure_washing.jinja',active_page = 'pressure_washing', service = services.get('pressure_washing'), buttons = buttons)
### end service routes ###


## other routes ###
@public.route('/about-us')
def about_us():
    return render_template('public/about_us.jinja', active_page = 'about_us')
@public.route('/financing')
def financing():
    return render_template('public/financing.jinja', active_page = 'financing')

@public.route('/contact-us', methods = ['GET', 'POST'])
def contact_us():
    """Handling full contact form, redirect to thank you if successful """

    form = ContactForm()
    if form.validate_on_submit():
        recaptcha_response = request.form.get('g-recaptcha-response')

        #verify the token with reCAPTCHA API
        verify_url = 'https://www.google.com/recaptcha/api/siteverify'
        payload = {'secret': current_app.config.get('RECAPTCHA_SECRET_KEY'), 'response': recaptcha_response, 'remoteip': request.remote_addr}
        current_app.logger.debug(f"reCAPTCHA payload: {{'secret': '*****', 'response': {payload['response']}, 'remoteip': {payload['remoteip']}}}")
        result = requests.post(verify_url, data = payload).json()

        if result.get('success'):
            if Contact.create_contact(form, complete=True):
                return redirect('/thank-you')
            else:
                flash('An error occurred while processing the form.')
        else:
            flash("Invalid reCAPTCHA. Please try again.", "danger")
            return redirect(url_for('public.contact_us') + '#ContactForm')
        
        #validation errors
        if form.errors:
            flash("There was an error with your submission. Please fill out required fields", "danger")
            return redirect(url_for('public.contact_us')  + '#ContactForm')

    return render_template('public/contact_us.jinja', active_page = 'contact_us', form = form)

@public.route('/thank-you')
def thank_you():
    """Thank you page for successful form submission"""
    return render_template('public/thank_you.jinja',active_page = 'thank_you')

@public.route('/gallery', methods = ['GET', 'POST'])
def gallery():
    """Process (Quick) contact form on this page"""
    form = ContactForm()
    
    if form.validate_on_submit():
        recaptcha_response = request.form.get('g-recaptcha-response')

        #verify the token with reCAPTCHA API
        verify_url = 'https://www.google.com/recaptcha/api/siteverify'
        payload = {'secret': current_app.config.get('RECAPTCHA_SECRET_KEY'), 'response': recaptcha_response, 'remoteip': request.remote_addr}
        current_app.logger.debug(f"reCAPTCHA payload: {{'secret': '*****', 'response': {payload['response']}, 'remoteip': {payload['remoteip']}}}")
        result = requests.post(verify_url, data = payload).json()

        if result.get('success'):
            if Contact.create_contact(form, complete=False):
                return redirect('/thank-you')
            else:
                flash('An error occurred while processing the form.')
        else:
            flash("Invalid reCAPTCHA. Please try again.", "danger")
            return redirect(url_for('public.gallery') + '#ContactForm')
        
        #validation errors
    if form.errors:
            flash("There was an error with your submission. Please fill out required fields", "danger")
            return redirect(url_for('public.gallery')  + '#ContactForm')
    
    return render_template('public/gallery.jinja', active_page = 'gallery', gallery_and_alt = gallery_and_alt, before_afters = before_afters, form = form)

# @public.route('/blogs')
# def blogs():
#     blogs = Blogs.query.all()
#     return render_template('public/blogs.jinja', blogs = blogs)

# @public.route('/blogs/<slug>')
# def blog_post(slug):
#     post = Blogs.query.filter_by(slug=slug).first_or_404()
#     return render_template('public/individual_blog_post.jinja', post = post )
