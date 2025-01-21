from database import db
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()

class Admin(db.Model):
    __tablename__ = 'admins'

    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    username = db.Column(db.String(50), unique = True, nullable = False)
    password = db.Column(db.String(300), nullable = False)
    is_admin = db.Column(db.Boolean, nullable = False, default = False) #True if admin

    @classmethod
    def create_admin(cls, username, password):
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
        return cls(username = username, password = hashed_password, is_admin = True) # type: ignore
        
    def set_password(self, new_password):
        if self.is_admin:
            self.password = bcrypt.generate_password_hash(new_password).decode('utf-8')
            return True
        return False
    
    @classmethod
    def authenticate_admin(cls, username, password):
        admin = Admin.query.filter_by(username = username).first()
        if admin and bcrypt.check_password_hash(admin.password,  password):
            return admin
        else:
            return None


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
    service_id = db.Column(db.Integer, db.ForeignKey('services.id'))


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
    address = db.Column(db.String(100))
    #foreign key
    service_type = db.Column(db.Integer, db.ForeignKey('services.id'))
    referral = db.Column(db.String(50))
    message = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=db.func.now())

    #relationship
    service = db.relationship('Services', backref='contacts')


