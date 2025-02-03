from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, migrate

db = SQLAlchemy()
migrate = None

def connect_db(app):
    """Connect to database"""
    global migrate
    db.init_app(app)
    migrate = Migrate(app, db)
