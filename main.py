""" The application is developed by Kittipich "Luke" Aiumbhornsin
Created on May 5, 2023
Run file of the application """

from wedeeoh_app import create_app
from decouple import config as en_var # import the environment var

app = create_app()

if __name__ == '__main__' :
    app.run(debug= en_var("debug") or False, port= en_var("port") or 8000)
