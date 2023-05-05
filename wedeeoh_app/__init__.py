# Root file of the `wedeeoh`
from flask import Flask, Blueprint, render_template, abort, flash, session
from decouple import config as en_var # import the environment var
from datetime import timedelta

TIMEOUT = timedelta(hours=1)
try:
    PORT = en_var("port")
except:
    PORT = 8000

def create_app():
    DOMAIN = f"lukecreated.com:{PORT}"
    app = Flask(__name__)
    app.config['SECRET_KEY'] = en_var('wedeeoh') # encrepted with Environment Variable
    app.config['REMEMBER_COOKIE_SECURE'] = True
    app.config['PERMANENT_SESSION_LIFETIME'] = TIMEOUT # set session timeout (need to use with before_request() below)
    app.config['TIMEZONE'] = 'Asia/Bangkok'
    app.config['SERVER_NAME'] = DOMAIN

    from .views.errorHandling import not_found, bad_request # import errors views
    from .views.views import views # import views

    app.register_blueprint(rootView, url_prefix='/')
    app.register_blueprint(views, url_prefix='/wedeeoh')
    app.register_error_handler(404, not_found)
    app.register_error_handler(400, bad_request)
    
    # cookies
    @app.before_request
    def before_request():
        pass

    return app

# this part for app info
class About():
    version = float()
    status = str()
    build = int()
    version_note = str()

    def __init__(self, version: float = float(0.0), status: str = 'None Stated', build: int = 20230500, version_note: str = "None Stated"):
        self.version = version
        self.status = status
        self.build = build
        self.version_note = version_note

    def __str__(self) -> str:
        return str("{ " + f"Version: {self.version} | Status: {self.status} | Build: {self.build} | Updates: {self.version_note}" + " }")

    def getSystemVersion(self) -> str:
        return str(self.version)

systemInfoObject = About(version=0.1, status='Initial development',
                         build=20230506, version_note='development starts')
systemInfo = systemInfoObject.__str__()
systemVersion = systemInfoObject.getSystemVersion()

# Below codes meant for development only
# subdomain `dev4wedeeoh` will not get access in production
rootView = Blueprint('rootView', __name__)
@rootView.route("/root-template-view/", subdomain='dev4wedeeoh')
def root_view():
    try: 
        return render_template("root.html")
    except:
        abort(403) # forbidden
