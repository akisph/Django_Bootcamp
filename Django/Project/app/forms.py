from django import forms
from django.core import validators
from app.models import User


class NewUserForm(forms.ModelForm):
    #if ou want to add any form validation you can overwrite the fields
    
    class Meta:
        model = User #this variable always has to named maodel
        fields = "__all__" 


