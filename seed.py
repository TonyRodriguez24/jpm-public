from models import User, Services, Projects, Reviews, Messages
from database import db
from app import app


services = [
            Services(name = 'ashpalt'), # type: ignore
            Services(name = 'concrete'), # type: ignore
            Services(name = 'home_improvement'), # type: ignore # type: ignore
            Services(name = 'masonry'), # type: ignore
            Services(name = 'paver_sealing'), # type: ignore
            Services(name = 'pressure_washing') # type: ignore
            ]

with app.app_context():
    db.drop_all()
    db.create_all()
    db.session.add_all(services)
    db.session.commit()

    print('Database created successfully')