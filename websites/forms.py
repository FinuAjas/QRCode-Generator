from dataclasses import fields
from pyexpat import model
from . models import Website
from django.forms import ModelForm

class WebsiteAddForm(ModelForm):
    class Meta:
        model = Website
        fields = ['name']

    def __init__(self,*args,**kwargs):
        super(WebsiteAddForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class':'form-control','placeholder':'Enter a website name to Generate QR Code.'})      
    