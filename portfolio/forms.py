from django import forms
from .models import Portfolio

class PortForm(forms.ModelForm):
    class Meta:
        model = Portfolio
        fields = ["text","media"]
        widgets = {
            "text": forms.TextInput(attrs={"class": "form-control"}),
            "media": forms.ClearableFileInput(),
        }
