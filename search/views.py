from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render,render_to_response
from django.template import RequestContext
from django.core.context_processors import csrf
from cra import *

def index(request):
  if 'details' in request.POST:
    details = request.POST['details']
    p=parse(str(details))
    print p
    return HttpResponse(p['price'])
  else:
    return render(request, 'search/index.html')
