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
    DOMAIN = f"showcases.lukecreated.com:{PORT}" # showcases.lukecreated.com
    app = Flask(__name__)
    app.config['SECRET_KEY'] = en_var('wedeeoh') # encrepted with Environment Variable
    app.config['REMEMBER_COOKIE_SECURE'] = True
    app.config['PERMANENT_SESSION_LIFETIME'] = TIMEOUT # set session timeout (need to use with before_request() below)
    app.config['SESSION_COOKIE_DOMAIN'] = False # prevent cookies to be access across domain and subdomain
    app.config['TIMEZONE'] = 'Asia/Bangkok'
    app.config['SERVER_NAME'] = DOMAIN

    from .views.errorHandling import not_found, bad_request # import errors views
    from .views.views import views # import views
    from .apis import api

    app.register_blueprint(dev, url_prefix='/')
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(api, url_prefix='/')
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

systemInfoObject = About(version=0.11, status='Initial development',
                         build=20230507, version_note='app infras implement')
systemInfo = systemInfoObject.__str__()
systemVersion = systemInfoObject.getSystemVersion()

# Below codes meant for development only
# subdomain `dev4wedeeoh` will not get access in production
dev = Blueprint('dev', __name__)
@dev.route("/root-template/", subdomain='dev4wedeeoh') # dev4wedeeoh.showcases.lukecreated.com
def root_view():
    try: 
        return render_template("root.html")
    except:
        abort(403) # forbidden
