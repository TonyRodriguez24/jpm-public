from models import User, Services, Projects, Reviews, Messages
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField
from wtforms.validators import DataRequired


class ContactForm(FlaskForm):
    first_name = StringField('First Name', 
                             validators=[DataRequired()],
                             render_kw={"placeholder": "Enter your first name"})
    last_name = StringField('Last Name',
                             validators=[DataRequired()],
                             render_kw={"placeholder": "Enter your last name"})
    phone = StringField('Phone Number', 
                        validators=[DataRequired()],
                        render_kw={"placeholder": "Enter your phone number"})
    email = StringField('Email Address',
                         validators=[DataRequired()],
                         render_kw={"placeholder": "Enter your email address"})
    address = StringField('Address', 
                          validators=[DataRequired()],
                          render_kw={"placeholder": "Enter your address"})

class SignUpForm(FlaskForm):


class LoginForm

class ReviewForm

class MessageForm

