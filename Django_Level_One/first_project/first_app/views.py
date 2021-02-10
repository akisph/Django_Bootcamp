from django.shortcuts import render 

from django.http import HttpResponse

# Create your views here.



def index(request): # each view takes at least one argument  
    my_dict = {
        'insert_me' : 'Hello I am from views.py'
    } # Sos we have to give every variable writen by jnga in the index.html file

    return render(request, 'first_app/index.html' , context = my_dict )



def help(request):
    help_dict = {'help_insert':'HELP PAGE'}
    return render(request, 'app/help.html', context = help_dict)    