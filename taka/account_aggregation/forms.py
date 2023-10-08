from django.forms import ModelForm
from django import forms
from .models import Account

class accountsform(ModelForm):
   
    class Meta:
        model = Account
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['description'].widget.attrs.update({'rows': '1'})