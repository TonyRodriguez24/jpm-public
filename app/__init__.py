from flask import Flask
import logging
from flask_login import current_user
from app.config import Config
from app.database import connect_db
from app.extensions import admin_login
from app.info import page_information, services
from app.routes import admin, public, seo, error

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    admin_login(app)
    connect_db(app)


# Capture DEBUG level and above 
# ranked in terms of serverity this is for logging.DEBUG it captures DEBUG and up
# CRITICAL 5 
# ERROR 4
# WARNING 3
# INFO 2 
# DEBUG 1


# Configure logging
    logging.basicConfig(
        level=logging.DEBUG,  
        format='%(asctime)s [%(levelname)s] %(message)s',  # time stamps , level name, and message
        handlers=[ #where it gets logged to 
            logging.FileHandler("error.log"),  # Log to a file
            logging.StreamHandler()  # can also log to the console
        ]
    )

    @app.context_processor
    def inject_globals():
        try:
            return {
                'services': services,
                'page_information': page_information,
                'current_user': current_user
            }
        except Exception as e:
            app.logger.error(f"Error in inject_globals: {e}")
            return {}

    app.register_blueprint(public)
    app.register_blueprint(admin)
    app.register_blueprint(seo)
    app.register_blueprint(error)

    return app