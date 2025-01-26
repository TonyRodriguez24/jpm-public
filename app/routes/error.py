from flask import Blueprint, render_template
from flask_login import current_user

error = Blueprint('error', __name__)

@error.errorhandler(404)
def page_not_found(e):
    """404 page"""
    # Render the 404 template with a 404 status code
    return render_template('error/404.jinja', current_user=current_user), 404

