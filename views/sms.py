from flask import Blueprint, render_template, request, session, redirect, jsonify
from modules.Connection import sqlite as con
import Configurations as c
import os

app = Blueprint("sms",__name__,template_folder='pages')

class sms:
	def __init__(self, arg):
		super(sms, self).__init__()
		self.arg = arg

	@app.route("/sms")
	def sms_view():
		return render_template('sms.html',mrms_url=c.URL_MRMS)