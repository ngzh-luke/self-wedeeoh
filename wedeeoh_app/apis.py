from . import systemInfo, systemVersion
from flask import Blueprint
from decouple import config as en_var # import the environment var

SUBDOMAIN = en_var("subdomain") or "wedeeoh" # if in dev then get from .env

api = Blueprint('api', __name__, subdomain=str(SUBDOMAIN)) 

@api.get("/return-wedeeoh-app-info/") # [SUBDOMAIN].showcases.lukecreated.com
def sysInfo(): # return string of system info
    return f"{systemInfo}"

@api.get("/return-wedeeoh-app-version/")
def sysVer(): # return string of system version
    return f"{systemVersion}"