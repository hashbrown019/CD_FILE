from flask import Blueprint, render_template, request, session, redirect, jsonify, send_file, send_from_directory
from modules.Connection import sqlite as con
from API.Models import models
import Configurations as c
import requests as req
import Strings as strs
import urllib.request
import json
import os

app = Blueprint("pdf" ,__name__ ,template_folder='pages')
bytes_str = b"{}"

class PDF:
	def __init__(self, arg):
		super(pdf, self).__init__()
		self.arg = arg

	@app.route('/show/<file>')
	def show_static_pdf(file):
		return send_from_directory(c.PDF_PATH,file)

	@app.route('/wait/<i>')
	def waits(i):
		msg = '''
			<h3 class='x-center x-text-grey'>
				PDF not available, Check if<br>
				- You are connected to Global Protect<br>
				- You are Connected to the Internet
				- You are in the Local network
				<span class='fa fa-eye-slash x-text-red'></span>
			</h3>'''
		return msg

	@app.route("/search",methods=["POST"])
	def search():
		search_item = request.form['item']
		pdf_list = req.get(c.DOMAIN+"*pdf")
		search_res = []
		pdfs = json.loads(pdf_list.text)
		for pdf in pdfs:
			if search_item.lower() in str(pdf).lower():
				search_res.append(pdf)
		return jsonify(search_res)

	@app.route("/get_all_doc_name",methods = ["POST"])
	def get_all_doc_name():
		res = models.get_all_doc_name()
		return jsonify({i:res.count(i) for i in res})

	@app.route("/get_all_modality",methods = ["POST"])
	def get_all_modality():
		res = models.get_all_modality()
		return jsonify({i:res.count(i) for i in res})

	@app.route("/get_meta_data")
	def get_meta_data():
		return jsonify(models.get_meta_data())

	@app.route("/get_comp",methods = ["POST"])
	def get_comp(): return jsonify(models.get_data_change())

	@app.route("/get_data_for_dash",methods = ["POST"])
	def get_data_for_dash(): return (models.get_meta_data())


	@app.route("/get_findings",methods = ["POST"])
	def get_findings():
		find = {}
		findings = models.get_data_mrms_findings()['mrms_findings']
		f_id = request.form['f_id']
		for f in findings:
			if str(f_id) in str(f['fk_file_guid']):
				find.update(f)
		return jsonify(find)

	@app.route("/search_v",methods=["POST"])
	def search_v():
		d_counter = 0
		v_res = ""
		search_item = request.form['item']
		pdf_list = models.get_data()
		search_res = []
		for pdf in pdf_list:
			if search_item.lower() in str(pdf).replace(''' " '''," ").lower():
				if d_counter <= c.LIMIT_SEARCH_RES:
					color = "red"
					if pdf['with_findings'] == None or pdf['with_findings']=='no findings': color = "green"
					v_res = v_res + strs.search_res_new.format(
						color,
						pdf['file_path'],
						pdf['file_id'],
						pdf['form_name'],
						pdf['activity_name'].split(".")[0],
						pdf['date_uploaded'],
						pdf['mun_name'],
						pdf['brgy_name'],
						pdf['modality_name'].upper(),
						pdf['cycle_name'].upper(),
						pdf['cadt_name']
						)
				else: continue
			d_counter += 1
		return v_res

	@app.route("/findings_search",methods=["POST"])
	def findings_search():
		d_counter = 0
		v_res = ""
		search_item = request.form['item']
		cfms_findings = models.get_data_cfms_json()['NCDDP']
		search_res = []
		for findings in cfms_findings:
			if search_item.lower() in str(findings['rfr_list']).replace(''' " '''," ").lower():
				v_res = v_res + strs.finding_res.format(
					str(findings['rfr_list']['findings_list']).replace('''"''',"|").replace("'","^"),
					findings['rfr_list']['sp_title'],
					findings['rfr_list']['brgy_name'],
					findings['rfr_list']['city_name'],
					findings['rfr_list']['prov_name'],
					len(findings['rfr_list']['findings_list']),
					findings['rfr_list']['bank_name'],
					findings['rfr_list']['tranche'],
					findings['rfr_list']['date_encoded'],
					findings['rfr_list']['dv_number'],
					findings['rfr_list']['sp_id'],
					findings['rfr_list']['rfr_id'],
					)
			d_counter += 1
		return v_res

