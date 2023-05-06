from flask import render_template, Blueprint, abort
from decouple import config as en_var # import the environment var

SUBDOMAIN = en_var("subdomain") or "wedeeoh" # if in dev then get from .env

views = Blueprint('views', __name__, subdomain=str(SUBDOMAIN)) # [SUBDOMAIN].showcases.lukecreated.com

@views.route('/')
@views.route('/home/')
@views.route('/index/')
def main():
    return render_template('main.html')

@views.route('/test/')
def f00():
    return abort(400)