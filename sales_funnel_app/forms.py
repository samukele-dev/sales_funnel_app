from django import forms
from .models import Lead

class LeadCreationForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = ['company','name', 'email', 'phone']
