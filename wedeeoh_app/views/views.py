from flask import render_template, Blueprint
from .. import systemInfo, systemVersion

views = Blueprint('views', __name__)

@views.route('/')
@views.route('/home/')
@views.route('/index/')
def main(): 
    return render_template('main.html', about=systemInfo, systemVersion=systemVersion)
