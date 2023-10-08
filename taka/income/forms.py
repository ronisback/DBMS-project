from django.forms import ModelForm
from django import forms
from .models import Income
from django.contrib.admin.widgets import AdminDateWidget

class incomeform(ModelForm):
    date = forms.DateField(
        widget=forms.DateInput(
            attrs={
                'type':'date'
            }
        )
    )
    class Meta:
        model = Income
        fields = '__all__'
        

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['description'].widget.attrs.update({'rows': '1'})
        