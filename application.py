from flask import Flask
from flask_cors import CORS

application = Flask(__name__)
cors = CORS(application)
application.config['CORS_HEADERS'] = 'Content-Type'
application.config['CORS_ORIGIN'] = '*'
application.config['CORS_ACCESS_CONTROL_ALLOW_ORIGIN'] = '*'

@application.route("/")
def index():
    return "Vodacom network incident"

if __name__ == '__main__': 
    from api import *
    application.run(host="0.0.0.0",port=80,debug=True,use_reloader=True)