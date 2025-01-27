import os
from dotenv import load_dotenv
load_dotenv()

class Config:
    SENDGRID_API_KEY = os.getenv("SENDGRID_API_KEY")
    SECRET_KEY = os.environ.get("SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI")
    RECAPTCHA_SECRET_KEY = os.getenv("RECAPTCHA_SECRET_KEY")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    ASSETS_DEBUG = False
    ENV = 'production'

