from django.shortcuts import render 

from django.http import HttpResponse
from first_app.models import Topic,Webpage,AccessRecord # import the models to views so we can get data 
from . import forms
# Create your views here.



def index(request): # each view takes at least one argument  
    webpages_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records':webpages_list}
    
    
    # Sos we have to give every variable writen by jnga in the index.html file
    return render(request, 'first_app/index.html' , context = date_dict )



def form_name_view(request):
    form = forms.FormName()

    if request.method == 'POST':
        form = forms.FormName(request.POST)

        if form.is_valid():
            print('VALIDTION SUCCESS')
            print('Name'+form.cleaned_data['name'])
            print('Name'+form.cleaned_data['email'])
            print('Name'+form.cleaned_data['text'])


    return render(request, 'first_app/form_page.html',{'form':form})
