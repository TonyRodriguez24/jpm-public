import unittest
from app import create_app
from app.models import Admin, Services, Projects, Reviews, Contact
from app.database import db

class TestModels(unittest.TestCase):
    def setUp(self):
        """Set up for each test"""
        self.app = create_app()
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///jpm'
        self.app.config['TESTING'] = True
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        """Clean up after each test"""
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_admin_creation(self):
        """Test making admin"""
        admin = Admin.create_admin(username='tony497', password='password123')
        db.session.add(admin)
        db.session.commit()

        test_admin = Admin.query.filter_by(username='tony497').first()
        self.assertIsNotNone(test_admin)
        self.assertNotEqual(test_admin.password, 'password123') # type: ignore

    def test_admin_auth(self):
        """Test admin authentication"""
        admin = Admin.create_admin(username='admin2', password='password123')
        db.session.add(admin)
        db.session.commit()

        # Correct password
        self.assertIsNotNone(Admin.authenticate_admin('admin2', 'password123'))

        # Incorrect password
        self.assertIsNone(Admin.authenticate_admin('admin2', 'wrongpassword'))

    def test_contact_creation(self):
        """Test Contact model"""
        service = Services(name='Concrete') # type: ignore
        db.session.add(service)
        db.session.commit()

        contact = Contact( name='Nick Moore', phone='123-456-7890', email='nmoore@example.com', service_type=service.id, address='123 Elm Street', referral='Google', message='Need pool repair' # type: ignore
        )
        db.session.add(contact)
        db.session.commit()

        test_contact = Contact.query.filter_by(email='nmoore@example.com').first()
        self.assertIsNotNone(test_contact)
        self.assertEqual(test_contact.name, 'Nick Moore') # type: ignore
        self.assertEqual(test_contact.service_type, service.id) # type: ignore
