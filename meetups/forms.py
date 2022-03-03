from dataclasses import field
from django import forms
# from .models import Participant

class RegistrationForm(forms.Form):
    # forms.ModelForm
    # class Meta:
    #     model = Participant
    #     fields = ['email']
    email = forms.EmailField(label='Your email')