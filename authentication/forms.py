from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, Event

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2', 'role']


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'first_name', 'last_name']

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = [
            'title', 'date', 'start_time', 'end_time', 'location',
            'description', 'organizer', 'event_type', 'link'
        ]
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control bg-white'}),
            'date': forms.DateInput(attrs={'class': 'form-control bg-white', 'type': 'date'}),
            'start_time': forms.TimeInput(attrs={'class': 'form-control bg-white', 'type': 'time'}),
            'end_time': forms.TimeInput(attrs={'class': 'form-control bg-white', 'type': 'time'}),
            'location': forms.TextInput(attrs={'class': 'form-control bg-white'}),
            'description': forms.Textarea(attrs={'class': 'form-control bg-white', 'rows': 3}),
            'organizer': forms.TextInput(attrs={'class': 'form-control bg-white'}),
            'event_type': forms.TextInput(attrs={'class': 'form-control bg-white'}),
            'link': forms.URLInput(attrs={'class': 'form-control bg-white'}),
        }