from flask import Flask, session, jsonify, request, redirect
from modules.Connection import sqlite as con
from flask_cors import CORS
import Configurations as c

from views import dash, sms
from API.REST import utils, back_end

app = Flask(__name__)
app.secret_key=c.SECRET_KEY
cors = CORS(app)

app.register_blueprint(utils.app)
app.register_blueprint(back_end.app)
app.register_blueprint(dash.app)
app.register_blueprint(sms.app)

@app.route("/")
def index():
	return redirect("/dash")

@app.route("/sms")
def sms():
	return redirect("/dash")

app.run(host=c.HOST,port=c.PORT,debug=c.IS_DEBUG)
		