from django.http import *
from django.shortcuts import render_to_response
from django.utils.encoding import *

from django.core.context_processors import csrf
import json, httplib, urllib



def http_post(url, path, params):
	conn = httplib.HTTPSConnection(url)
	headers = {"Content-type": "application/x-www-form-urlencoded",
			"Accept": "text/plain"}
	params = urllib.urlencode(params)
	conn.request("POST", path, params, headers)	
	res = conn.getresponse().read()
	return json.loads(res)


def auth(request):
	try:
		code = request.GET["code"]
		state = request.GET["state"]
		params = {'grant_type' : 'authorization_code', 
				'code': code, 
				'redirect_uri': 'http://anantb.csail.mit.edu:8000/auth', 
				'client_id': 'o0ezp27jbqro', 
				'client_secret':'VwSszmPmDs1YeZLz',
				'state':state}
		res = http_post("www.linkedin.com", '/uas/oauth2/accessToken', params)
		return HttpResponse(json.dumps(res), mimetype="application/json")
	except Exception, e:
		res = {'status': 'Error'}
		res['error'] = e
		return HttpResponse(json.dumps(res), mimetype="application/json")


def home(request):
	return render_to_response('home.html')