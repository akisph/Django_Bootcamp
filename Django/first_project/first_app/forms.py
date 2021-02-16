from django import forms
from django.core import validators # 2nd valiudation way
from first_app.models import Topic,Webpage,AccessRecords

# in case you want to make an custom validation 
# you ll need to make a function outside of the 
# class
def check_for_z(value): #must always pass this variable "value"
    """validator check if the first letter of a value is z"""
    if value[0].lower() != 'z':
        raise forms.ValidationError('The field needs to start with z')

class FormName(forms.Form):
    # there are three basic inpouts

    name = forms.CharField(validators=[check_for_z])
    email = forms.EmailField()
    verify_email = forms.EmailField(label='Enter your email again')
    text = forms.CharField(widget = forms.Textarea)
    botcatcher = forms.CharField(required = False,
                                widget = forms.HiddenInput,
                                validators=[validators.MaxLengthValidator(0)]) # instead of clean method you can use validators



    def clean(self):
        '''3rd way by this clean function with super you can make all validation in one function '''
        all_clean_data = super().clean()
        email = all_clean_data['email']
        vemail = all_clean_data['verify_email']
        if email != vemail:
            raise forms.ValidationError('The emails dont match')



    # def clean_botcatcher(self):
    #     # 1st way
    #     # the django will search for clean methods automatically
    #     botcatcher = self.cleaned_data['botcatcher']
    #     if len(botcatcher) > 0:
    #         raise forms.ValidationError("We hit a bot")
    #     return botcatcher
