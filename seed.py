from models import Services, Admin
from database import db
from app import app

services = [Services(name = 'asphalt'), Services(name = 'concrete'), Services(name = 'home_improvement'), Services(name = 'masonry'), Services(name = 'paver_sealing'), Services(name = 'pressure_washing')] # type: ignore

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