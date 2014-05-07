from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render,render_to_response
from django.template import RequestContext
from django.core.context_processors import csrf
from cra import *
from search.forms import *

def index(request):
  '''
    This view takes the entry url and use it in the script to get values and then displays the data , i.e, p here
  '''
  form = url_form()
  if request.method == 'POST':
    form = url_form(request.POST)
    if form.is_valid(): 
      details =form.cleaned_data['content']
      p=parse(details)
    return render_to_response('search/result.html',{'form':form,
                     'p':p  }, context_instance=RequestContext(request))
  
  else:
    form = url_form()
    return render_to_response('search/index.html',{'form':form}, context_instance=RequestContext(request))
