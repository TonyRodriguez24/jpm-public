from database import db

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    username = db.Column(db.String(50), unique = True, nullable = False)
    email = db.Column(db.String(100), nullable = False, unique = True)
    password = db.Column(db.String(300), nullable = False)

#in seed py
class Services(db.Model):
    __tablename__ = 'services'

    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    name = db.Column(db.String(50), nullable = False, unique = True)

class Projects(db.Model):
    __tablename__ = 'projects'

    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    type_of_work = db.Column(db.String(50), nullable = False)

    #foreign keys
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    service_id = db.Column(db.Integer, db.ForeignKey('services.id'))

    #relationships
    user = db.relationship('User', backref = 'projects')

class Reviews(db.Model):
    __tablename__ = 'reviews'

    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    rating = db.Column(db.Integer, nullable = False)
    message = db.Column(db.Text(), nullable = True)

    #foreign key
    service_id = db.Column(db.Integer, db.ForeignKey('services.id'))

class Contact(db.Model):
    __tablename__ = 'messages'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    phone = db.Column(db.String(30), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(100), nullable = False)
    #foreign key
    service_type = db.Column(db.Integer, db.ForeignKey('services.id'))
    message = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.now())

    #relationship
    service = db.relationship('Services', backref='contacts')


