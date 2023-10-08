from django.forms import ModelForm
from .models import Bill
from django import forms

class billform(ModelForm):
    due_date = forms.DateField(
        widget=forms.DateInput(
            attrs={
                'type':'date'
            }
        )
    )
    class Meta:
        model = Bill
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['description'].widget.attrs.update({'rows': '1'})