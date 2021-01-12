import json
from flask import jsonify
import urllib.request
import Configurations as c

def get_data_change():
	datum_store = json.loads(open('assets/json/mrms.json','r').read())
	mrms_store = get_data_mrms()
	datum_store_findings = json.loads(open('assets/json/findings.json','r').read())
	mrms_store_findings = get_data_mrms_findings()
	comp = [
			len(datum_store['mrms_files']),
			len(mrms_store['mrms_files']),
			len(datum_store_findings['mrms_findings']),
			len(mrms_store_findings['mrms_findings'])
			]
	return comp

def get_data():
	datum = json.loads(open('assets/json/mrms.json','r').read())
	return datum['mrms_files']

def get_data_mrms_findings():
	datum = json.loads(open('assets/json/findings.json','r').read())
	return datum['mrms_findings']

def get_data_mrms():
	u = urllib.request.urlopen(c.URL_API_MRMS).read()#The url you want to open
	dec_u = (json.loads(u.decode('utf-8')))
	# res_ = (dec_u['mrms_files'])
	return dec_u

def get_data_mrms_findings():
	u = urllib.request.urlopen(c.URL_API_MRMS_FINDINGS).read()#The url you want to open
	dec_u = (json.loads(u.decode('utf-8')))
	# res_ = (dec_u['mrms_files'])
	return dec_u

def get_data_cfms_web():
	u = urllib.request.urlopen(c.URL_CFMS_RFR).read()#The url you want to open
	dec_u = (json.loads(u.decode('utf-8')))
	# res_ = (dec_u['mrms_files'])
	return dec_u

def get_data_cfms_json():
	datum = json.loads(open('assets/json/cfms_rfr.json','r').read())
	return datum

def get_meta_data():
	tree = {}
	mun = []
	brgy = []
	modal = []
	cycle = []

	for meta in get_data():
		mun.append(meta['mun_name'])
		brgy.append(meta['brgy_name'])
		modal.append(meta['modality_name'].upper())
		cycle.append(meta['cycle_name'].upper())
		if meta['mun_name'] in tree: pass
		else: tree.update({meta['mun_name']:[]})
		if meta['brgy_name'] in tree[meta['mun_name']]: pass
		else: tree[meta['mun_name']].append(meta['brgy_name'])

	meta = [{
				'all_mun':list(dict.fromkeys(mun)),
				'all_mun_number':len(mun),
				'all_mun_entry':len(list(dict.fromkeys(mun)))
			},
			{
				'all_brgy':list(dict.fromkeys(brgy)),
				'all_brgy_number':len(brgy),
				'all_brgy_entry':len(list(dict.fromkeys(brgy)))
			},
			{
				'all_modal':list(dict.fromkeys(modal)),
				'all_modal_number':len(modal),
				'all_modal_entry':len(list(dict.fromkeys(modal)))
			},
			{
				'all_cycle':list(dict.fromkeys(cycle)),
				'all_cycle_number':len(cycle),
				'all_cycle_entry':len(list(dict.fromkeys(cycle)))
			}]
			
	open("samp.json",'w').write(str(tree).
		replace("none","'########'").
		replace('None',"'########'").
		replace("null","'########'").
		replace("Null","'########'").
		replace("'",'''"'''))
	return (open("samp.json",'r').read())
	# return get_data()

def get_locations():
	with open("assets/json/locations.json") as myjsonfile:
		return json.load(myjsonfile) 

def get_all_doc_name():
	form_name = []
	for datum in get_data():
		form_name.append(datum['activity_name'].replace("\n","").replace("\r","").upper())
	return (form_name)

def get_all_modality():
	form_name = []
	for datum in get_data():
		form_name.append(datum['modality_name'].replace("\n","").replace("\r","").upper())
	return (form_name)