from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render,render_to_response
from django.template import RequestContext
from django.core.context_processors import csrf
from cra import *

def index(request):
  '''
    This view takes the entry url and use it in the script to get values and then displays the data , i.e, p here
  '''

  if 'details' in request.POST:
    details = request.POST['details']
    p=parse(str(details))
    print p
    import pdb; pdb.set_trace;
    return HttpResponse(p['image'])
#    return render_to_response('search/index.html', p , context_instance=RequestContext(request))
  else:
    return render(request, 'search/index.html')
