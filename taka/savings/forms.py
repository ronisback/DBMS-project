from django.forms import ModelForm
from .models import Savings
from django import forms

class savingsform(ModelForm):
    date = forms.DateField(
        widget=forms.DateInput(
            attrs={
                'type':'date'
            }
        )
    )
    class Meta:
        model = Savings
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['description'].widget.attrs.update({'rows': '1'})