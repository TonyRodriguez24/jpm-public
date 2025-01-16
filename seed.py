from models import Services, Admin
from database import db
from app import app


services = [
            Services(name = 'asphalt'), # type: ignore
            Services(name = 'concrete'), # type: ignore
            Services(name = 'home_improvement'), # type: ignore # type: ignore
            Services(name = 'masonry'), # type: ignore
            Services(name = 'paver_sealing'), # type: ignore
            Services(name = 'pressure_washing') # type: ignore
            ]

admin1 = Admin.create_admin(username="nmoore99", password='sds.edu')
admin2 = Admin.create_admin(username="tonyrodriguez24", password='sds.edu')

with app.app_context():
    db.drop_all()
    db.create_all()
    db.session.add_all(services)
    db.session.commit()
    
    db.session.add(admin1)
    db.session.add(admin2)
    db.session.commit()


    print('Database created successfully')