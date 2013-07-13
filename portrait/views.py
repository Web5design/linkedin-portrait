from django.http import *
from django.shortcuts import render_to_response
from django.utils.encoding import *

from django.core.context_processors import csrf
import json



def auth(request):
	return HttpResponseRedirect("https://www.linkedin.com/uas/oauth2/authorization?\
		response_type=code&client_id=%s&scope=%s&state=%s&redirect_uri=%s" 
		%("o0ezp27jbqro","r_fullprofile%20r_emailaddress%20r_network","linkedin_hackathon2013_portrait", "http://anantb.csail.mit.edu:8000/auth_verify"))


def auth_verify(request):
	res = {'status': 'Error'}
	try:
		res['code'] = request.GET["code"]
		res['state'] = request.GET["state"]
		res['status'] = 'OK'
		return HttpResponse(res, mimetype="application/json")
	except Exception, e:
		res['error'] = request.GET["error"]
		res['error_description'] = request.GET["error_description"]
		return HttpResponse(res, mimetype="application/json")


def home(request):
	return HttpResponse('Trisha is cool!')