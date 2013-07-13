from django.http import *
from django.shortcuts import render_to_response
from django.utils.encoding import *

from django.core.context_processors import csrf
import json



def auth(request):
	res = {'status': 'Error'}
	try:
		res['code'] = request.GET["code"]
		res['state'] = request.GET["state"]
		res['status'] = 'OK'
		return HttpResponse(json.dumps(res), mimetype="application/json")
	except Exception, e:
		res['error'] = request.GET["error"]
		res['error_description'] = request.GET["error_description"]
		return HttpResponse(json.dumps(res), mimetype="application/json")


def home(request):
	return render_to_response('home.html')