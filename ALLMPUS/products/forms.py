'''from django.contrib.auth import forms
from django import forms
from .models import rfq
class getquote(forms.ModelForm):
    class Meta:
        model = rfq
        fields = ('name', 'email', 'company', 'contact','package','package_unit' )
        labels = {'name':'NAME','email': 'EMAIL','contact':'CONTACT','Package':'PACKAGE'} '''