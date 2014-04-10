from search.forms import *
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render,render_to_response
from django.template import RequestContext
from django.core.context_processors import csrf

def index(request):
   if request.method == 'GET':
      form = url_form()
   else:
      form=url_form(requset.POST)
     
      if form.is_valid():
        content = form.cleaned_data['content']
        post=m.Post.objects.create(content=content)
        return render(request,'/search/index.html') 

   return render_to_response(request, '/search/index.html',{
                'form': form,},context_instance = RequestContext(request)) 
