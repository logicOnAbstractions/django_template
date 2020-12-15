from django import forms
from .models import MyObjects

class CreateElement(forms.ModelForm):
    class Meta:
        model = MyObjects
        fields = ["name"]
