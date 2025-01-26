from flask_compress import Compress
from flask_assets import Environment, Bundle
from flask_login import LoginManager
from app.models import Admin


login_manager = LoginManager()

Compress()
assets = Environment()

css = Bundle('contact_us.css', 'gallery.css', 'global.css', 'home.css', filters='cssmin', output='dist/css/styles.min.css')
js = Bundle('app.js', 'gallery.js', filters='jsmin', output='dist/scripts.min.js')

def compress_assets(app):
    assets.init_app(app)
    assets.auto_build = True # builds bundles automatically on app startup
    assets.debug = False
    assets.register('css_all', css)
    assets.register('js_all', js)

def admin_login(app):
    login_manager.init_app(app)
    login_manager.login_view = 'admin.login'  # type: ignore # Redirect to 'admin' login route for unauthenticated users
    login_manager.login_message = 'Please log in as an admin to access this page.'
    login_manager.login_message_category = 'danger'

@login_manager.user_loader
def load_user(admin_id):
    return Admin.query.get(int(admin_id))