from app.models import Services, Admin
from app.database import db
from sqlalchemy import text
from app import create_app

app = create_app()

def seed_database():
    try:
        with app.app_context():
            # Reset database schema
            db.session.execute(text("DROP SCHEMA public CASCADE;"))
            db.session.execute(text("CREATE SCHEMA public;"))
            db.session.commit()

            # Create all tables
            db.create_all()

            # Add services
            services = [Services(name="asphalt"),Services(name="concrete"), Services(name="home_improvement"), Services(name="masonry"), Services(name="paver_sealing"), Services(name="pressure_washing"),] # type: ignore
            db.session.add_all(services)
            db.session.commit()

            # Add admins
            admin1 = Admin.create_admin(username="nmoore99", password="jpm@sds.edu")
            admin2 = Admin.create_admin(username="tonyrodriguez24", password="jpm@sds.edu")
            db.session.add(admin1)
            db.session.add(admin2)
            db.session.commit()

            print("Database created and seeded successfully!")
    except Exception as e:
        print(f"Error during database seeding: {e}")
        db.session.rollback()

if __name__ == "__main__":
    seed_database()
