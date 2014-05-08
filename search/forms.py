from django import forms

class url_form(forms.Form):
     content=forms.CharField()

class url_ind_form(forms.Form):
     url = forms.CharField()
     xpath1 = forms.CharField()
     xpath2 = forms.CharField()
     xpath3 = forms.CharField()
