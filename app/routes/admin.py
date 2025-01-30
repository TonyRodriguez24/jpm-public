from flask import Blueprint, flash, redirect, render_template, session, url_for
from app.database import db
from app.forms import ContactForm, LoginForm, ProjectForm, SetPasswordForm
from app.models import Admin, Contact, Projects, get_column_names
from flask_login import login_user, login_required, logout_user, current_user

admin = Blueprint('admin', __name__, url_prefix = '/admin')

@admin.route('/login', methods = ['GET', 'POST'])
def login():
    """Login form and adding is_admin to session for navbar purposes of current_user.is_authenticated not working"""
    form = LoginForm()

    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data

        admin = Admin.authenticate_admin(username = username, password = password)

        if admin:
            session['is_admin'] = True
            login_user(admin)
            flash('You are successfully logged in', 'success')
            return redirect(url_for('admin.dashboard'))
        else:
            flash('Incorrect password/username', 'danger')

    return render_template('admin/login.jinja', form = form, active_page = 'login')

@admin.route('/dashboard', methods = ['GET','POST'])
@login_required
def dashboard():
    """Dashboard of all contacts and projects for an admin user to interact with"""

    admin = current_user

    contacts = Contact.query.all()
    contact_table_headers = get_column_names(Contact)
    projects = Projects.query.all()

    return render_template('admin/dashboard.jinja', active_page = 'dashboard', admin = admin, contacts = contacts, table_headers = contact_table_headers, projects = projects)

@admin.route('/set-password', methods=['GET', 'POST'])
@login_required
def set_password():
    """ Allow the logged-in admin to update password """

    form = SetPasswordForm()
    if form.validate_on_submit():
        new_password = form.new_password.data

        try:
            current_user.set_password(new_password)
            db.session.commit()
            flash('Password successfully updated.', 'success')
            return redirect(url_for('admin.dashboard'))
        except Exception as e:
            db.session.rollback()
            flash(f'An error occurred: {str(e)}', 'danger')

    return render_template('admin/set_password.jinja', form=form, active_page='set_password')

@admin.route('/add-contact', methods=['GET', 'POST'])
@login_required
def add_contact():
    """Form for admin adding a contact instead of through form submission"""

    form = ContactForm()
    if form.validate_on_submit():
        # Create a new Contact instance
        new_contact = Contact(
            name=form.name.data,phone=form.phone.data,email=form.email.data,address=form.address.data,service_type=form.service_type.data,message=form.message.data # type: ignore
        )

        # Save the new contact to the database
        db.session.add(new_contact)
        db.session.commit()

        flash('New contact added successfully!', 'success')
        return redirect(url_for('admin.dashboard'))

    return render_template('admin/contacts/add_contact.jinja', form=form)

@admin.route('/edit-contact/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_contact(id):
    """Edit contact form for admin"""
    contact = Contact.query.get_or_404(id)

    # Prepopulate the form with the contact's existing data
    form = ContactForm(obj=contact)

    if form.validate_on_submit():
        # Update contact with form data
        contact.name = form.name.data
        contact.email = form.email.data
        contact.address = form.address.data
        contact.service_type = form.service_type.data
        contact.message = form.message.data
        contact.phone = form.phone.data

        # Save changes to the database
        db.session.commit()
        flash('Contact updated successfully!', 'success')
        return redirect(url_for('admin.dashboard'))

    return render_template('admin/contacts/edit_contact.jinja', form=form)

@admin.route('/delete-contact/<int:id>', methods = ['POST'])
@login_required
def delete_contact(id):
    """Deleting contact for admin, post route only"""

    contact = Contact.query.get_or_404(id)
    db.session.delete(contact)
    db.session.commit()
    flash('Contact succesfully removed', 'success')
    return redirect(url_for('admin.dashboard'))

@admin.route('/delete-all-contacts', methods=['POST'])
@login_required
def delete_all_contacts():
    """Deleting all contacts for admin, post route only"""
    # Delete all contacts
    Contact.query.delete()
    db.session.commit()

    # Redirect with a success message
    flash('All contacts have been deleted.', 'success')
    return redirect(url_for('admin.dashboard'))

@admin.route('/add-project', methods=['GET', 'POST'])
@login_required
def add_project():
    """Form for admin adding a project *needs to be fleshed out"""

    form = ProjectForm()
    if form.validate_on_submit():
        # Create a new project
        new_project = Projects(
            type_of_work=form.type_of_work.data, # type: ignore
            service_id=form.service_id.data # type: ignore
        )
        db.session.add(new_project)
        db.session.commit()
        flash('New project added successfully!', 'success')
        return redirect(url_for('admin.dashboard'))

    return render_template('admin/projects/add_project.jinja', form=form, title='Add Project')

@admin.route('/edit-project/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_project(id):
    """Form for admin editing a project"""

    project = Projects.query.get_or_404(id)
    form = ProjectForm(obj=project)

    if form.validate_on_submit():
        # Update the project with form data
        project.type_of_work = form.type_of_work.data
        project.service_id = form.service_id.data

        db.session.commit()
        flash('Project updated successfully!', 'success')
        return redirect(url_for('admin.dashboard'))

    return render_template('admin/projects/edit_project.jinja', form=form, title='Edit Project', project=project)

@admin.route('/delete-project/<int:id>', methods=['POST'])
@login_required
def delete_project(id):
    """Form for admin deleting a project"""

    project = Projects.query.get_or_404(id)
    db.session.delete(project)
    db.session.commit()
    flash('Project deleted successfully!', 'success')
    return redirect(url_for('admin.dashboard'))

@admin.route('/logout', methods = ['GET', 'POST'])
@login_required
def logout():
    """Logging out, pop is_admin from session and use flask login to log user out"""

    session.pop('is_admin', None)
    logout_user()
    flash('You have been logged out.', 'success')
    return redirect(url_for('admin.logout'))