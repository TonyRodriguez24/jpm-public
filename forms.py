import email
from email import contentmanager
from flask import Flask
from flask_wtf import FlaskForm
from wtforms import IntegerField, PasswordField, StringField, SelectField, EmailField, TextAreaField
from wtforms.validators import DataRequired


class ContactForm(FlaskForm):
    name = StringField('Name', 
                             validators=[DataRequired()],
                             render_kw={"placeholder": "Enter your name"})
    phone = StringField('Phone Number', 
                        validators=[DataRequired()],
                        render_kw={"placeholder": "Enter your phone number"})
    email = EmailField('Email Address',
                         validators=[DataRequired()],
                         render_kw={"placeholder": "Enter your email address"})
    address = StringField('Address', 
                          validators=[DataRequired()],
                          render_kw={"placeholder": "Enter your address"})
    
    service_type = SelectField("Service needed",
                               validators=[DataRequired()])

    message = TextAreaField("Message",
                            render_kw={"placeholder": "Tell us what you need! We are more than happy to help."})


class SignUpForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()], render_kw={"placeholder": "Enter your username"})

    password = PasswordField("Password", validators=[DataRequired()], render_kw={"placeholder": "Enter your password"})

    email = EmailField("Email", validators=[DataRequired()], render_kw= {"placeholder": "Enter your email address"})

class LoginForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()], render_kw={"placeholder": "Enter your username"})

    password = PasswordField("Password", validators=[DataRequired()], render_kw={"placeholder": "Enter your password"})


class ReviewForm(FlaskForm):
    rating = IntegerField("Rating", validators=[DataRequired()])

    message = TextAreaField("Message", render_kw={"placeholder": "Tell us about your experience, your feedback is important to us."})

    service_type = SelectField("Select the service you received")

