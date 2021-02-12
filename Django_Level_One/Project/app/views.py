from django.shortcuts import render
from django.http import HttpResponse
from app.models import User

# Create your views here.
def index(request):
    return HttpResponse('<em> My second App </em> ')


def help(request):
    help_dict = {'help_insert':'HELP PAGE'}
    return render(request, 'app/help.html', help_dict)

def users(request):    
    users_ = User.objects.all()
    user_inf = {
        'users_infos':users_
    }
    return render(request, 'app/users.html',user_inf)