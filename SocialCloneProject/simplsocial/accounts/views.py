from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy 
from django.views.generic import CreateView

from . import forms 

# Create your views here.


class SignUp(CreateView):
    
    form_class = form.UserCreateForm
    success_url = reverse_lazy('login') # When someone signup send them to LOGIN 
    template_name = 'account/signup.html'

