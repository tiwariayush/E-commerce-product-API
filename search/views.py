from search.forms import *

def url_form_process(request):
   if request.method == 'GET':
      form = url_form()
   else:
      form=url_form(requset.POST)
     
      if form.is_valid():
       content = form.cleaned_data['content']
