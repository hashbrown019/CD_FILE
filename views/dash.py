from flask import Blueprint, render_template, request, session, redirect, jsonify
from modules.Connection import sqlite as con
import Configurations as c
import os

app = Blueprint("dash",__name__,template_folder='pages')

class dash:
	def __init__(self, arg):
		super(dash, self).__init__()
		self.arg = arg

	@app.route("/dash")
	def dash_view():
		return render_template('dash.html',mrms_url=c.URL_MRMS)