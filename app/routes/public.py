from flask import Blueprint, current_app, flash, redirect, render_template, request, url_for
import requests
from app.forms import ContactForm
from app.models import Contact
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
        result = requests.post(verify_url, data = payload).json()

        if result.get('success'):
            if Contact.create_contact(form, complete=False):
                flash("Your form has been submitted. We try to get back to you the same day, expect a phone call or email from us.", "success")
                return redirect('/thank-you')
            else:
                flash('An error occurred while processing the form.')
        else:
            flash("Invalid reCAPTCHA. Please try again.", "danger")
            return redirect(url_for('public.home') + '#ContactForm')


    #validation errors
    if form.errors:
        flash("There was an error with your submission. Please fill out required fields", "danger")
        return redirect(url_for('public.home')  + '#ContactForm')

    # Render the home page with the form and any error messages
    return render_template('public/home.jinja', form=form, active_page='public.home')

### service routes - setting active page, getting service from services object, getting buttons from buttons object ###
@public.route('/asphalt')
def asphalt():
    return render_template('public/services/asphalt.jinja', active_page = 'public.asphalt', service = services.get('asphalt'), buttons = buttons)
@public.route('/concrete')
def concrete():
    return render_template('public/services/concrete.jinja', active_page = 'public.concrete', service = services.get('concrete'), buttons = buttons)
@public.route('/home-improvement')
def home_improvement():
    return render_template('public/services/home_improvement.jinja', active_page = 'public.home_improvement', service = services.get('home_improvement'), buttons = buttons)
@public.route('/masonry')
def masonry():
    return render_template('public/services/masonry.jinja', active_page = 'public.masonry', service = services.get('masonry'), buttons = buttons)
@public.route('/paver-sealing')
def paver_sealing():
    return render_template('public/services/paver_sealing.jinja', active_page = 'public.paver_sealing', service = services.get('paver_sealing'), buttons = buttons)
@public.route('/pressure-washing')
def pressure_washing():
    return render_template('public/services/pressure_washing.jinja',active_page = 'public.pressure_washing', service = services.get('pressure_washing'), buttons = buttons)
### end service routes ###


## other routes ###
@public.route('/about-us')
def about_us():
    return render_template('public/about_us.jinja', active_page = 'public.about_us')
@public.route('/financing')
def financing():
    return render_template('public/financing.jinja', active_page = 'public.financing')

@public.route('/contact-us', methods = ['GET', 'POST'])
def contact_us():
    """Handling full contact form, redirect to thank you if successful """

    form = ContactForm()
    if form.validate_on_submit():
        recaptcha_response = request.form.get('g-recaptcha-response')

        #verify the token with reCAPTCHA API
        verify_url = 'https://www.google.com/recaptcha/api/siteverify'
        payload = {'secret': current_app.config.get('RECAPTCHA_SECRET_KEY'), 'response': recaptcha_response, 'remoteip': request.remote_addr}
        result = requests.post(verify_url, data = payload).json()

        if result.get('success'):
            if Contact.create_contact(form, complete=True):
                flash("Your form has been submitted. We try to get back to you the same day, expect a phone call or email from us.", "success")
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

    return render_template('public/contact_us.jinja', active_page = 'public.contact_us', form = form)

@public.route('/thank-you')
def thank_you():
    """Thank you page for successful form submission"""
    return render_template('public/thank_you.jinja',active_page = 'public.thank_you')

@public.route('/gallery', methods = ['GET', 'POST'])
def gallery():
    """Process (Quick) contact form on this page"""
    form = ContactForm()
    
    if form.validate_on_submit():
        recaptcha_response = request.form.get('g-recaptcha-response')

        #verify the token with reCAPTCHA API
        verify_url = 'https://www.google.com/recaptcha/api/siteverify'
        payload = {'secret': current_app.config.get('RECAPTCHA_SECRET_KEY'), 'response': recaptcha_response, 'remoteip': request.remote_addr}
        result = requests.post(verify_url, data = payload).json()

        if result.get('success'):
            if Contact.create_contact(form, complete=False):
                flash("Your form has been submitted. We try to get back to you the same day, expect a phone call or email from us.", "success")
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
    
    return render_template('public/gallery.jinja', active_page = 'public.gallery', gallery_and_alt = gallery_and_alt, before_afters = before_afters, form = form)



