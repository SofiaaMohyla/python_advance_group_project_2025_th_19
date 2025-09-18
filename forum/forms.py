from django import forms
from .models import Branch, Massage

class BranchCreateForm(forms.ModelForm):
    class Meta:
        model = Branch
        fields = ['name', 'description']


class MassageCreateForm(forms.ModelForm):
    class Meta:
        model = Massage
        fields = ['massage']