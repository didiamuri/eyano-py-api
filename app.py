from flask import Flask, send_file
from flask_cors import CORS, cross_origin

flaskAppInstance = Flask(__name__)
cors = CORS(flaskAppInstance)
flaskAppInstance.config['CORS_HEADERS'] = 'Content-Type'
flaskAppInstance.config['CORS_ORIGIN'] = '*'
flaskAppInstance.config['CORS_ACCESS_CONTROL_ALLOW_ORIGIN'] = '*'

@flaskAppInstance.route("/")
def index():
    return "Vodacom network incident"

if __name__ == '__main__': 
    from api import *
    flaskAppInstance.run(host="0.0.0.0",port=80,debug=True,use_reloader=True)