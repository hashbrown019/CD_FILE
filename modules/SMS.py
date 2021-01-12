from vonage import Sms

VONAGE_API_KEY = "3177048c"
VONAGE_API_SECRET = "PsTifyun0ge1rEpA"
VONAGE_BRAND_NAME = "こ界"
TO_NUMBER = ""

sms = Sms(key=VONAGE_API_KEY, secret=VONAGE_API_SECRET)

class sms(object):
	def __init__(self, arg):
		super(sms, self).__init__()
		self.arg = arg
		

	def send_sms(num,msg,args):
		res = sms.send_message({
			"from": VONAGE_BRAND_NAME,
			"to": num,
			"text": msg,
		})
		return res