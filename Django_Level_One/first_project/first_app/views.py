from django.shortcuts import render 

from django.http import HttpResponse
from first_app.models import Topic,Webpage,AccessRecord # import the models to views so we can get data 
# Create your views here.



def index(request): # each view takes at least one argument  
    webpages_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records':webpages_list}
    
    
    # Sos we have to give every variable writen by jnga in the index.html file
    return render(request, 'first_app/index.html' , context = date_dict )

