import urllib.request
import shutil
from flask import Blueprint, render_template, request, session, redirect, jsonify
from modules.Connection import sqlite as con
from modules.PDF_Util import pdf as pdutil
from pyquery import PyQuery
import Configurations as c
import urllib
import os

app = Blueprint("util",__name__,template_folder='pages')

class util:
	def __init__(self, arg):
		super(user, self).__init__()
		self.arg = arg

	@app.route("/add_act",methods = ["POST","GET","OPTIONS"])
	def add_act():
		print(request.form)
		return "SUCCESS ADDING : {}".format(request.form)

	@app.route("/get_files_mrms",methods = ["POST","GET","OPTIONS"])
	def get_files_mrms():
		f = urllib.request.urlopen(c.URL_MRMS+"ncddp")
		res = f.read()
		pq = PyQuery(res)
		tag = pq('a')
		all_a_file = (tag.text().split(" "))
		all_a_file.pop(0)
		util.read_pdf_to_text(all_a_file[1])
		return res

	def read_pdf_to_text(filename):
		url = c.URL_MRMS+"ncddp/"+filename
		output_file = "assets/temp/temp.pdf"
		with urllib.request.urlopen(url) as response, open(output_file, 'wb') as out_file:
			OBJ = shutil.copyfileobj(response, out_file)
			print(response)
			print("-------------------")
			print(OBJ)
			print("-------------------")
			print(out_file)
		pdutil.pdfToImage(output_file,1)