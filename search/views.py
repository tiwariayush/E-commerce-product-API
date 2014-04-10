from search.forms import *
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render,render_to_response
from django.template import RequestContext
from django.core.context_processors import csrf

def index(request):
  if 'details' in request.POST:
    details = request.POST['details']
    return HttpResponse(details)
  else:
    return render(request, 'search/index.html')
