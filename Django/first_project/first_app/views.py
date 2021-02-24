from django.shortcuts import render 

from django.http import HttpResponse
from django.contrib.auth.models import User
from first_app.models import Topic,Webpage,AccessRecord,UserProfileInfo # import the models to views so we can get data 

from first_app.forms import UserForm,UserProfileInfoForm,FormName
# Create your views here.



def index(request): # each view takes at least one argument  
    webpages_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records':webpages_list}
    
    
    # Sos we have to give every variable writen by jnga in the index.html file
    return render(request, 'first_app/index.html' , context = date_dict )



def form_name_view(request):
    form = FormName()

    if request.method == 'POST':
        form = FormName(request.POST)

        if form.is_valid():
            print('VALIDTION SUCCESS')
            print('Name'+form.cleaned_data['name'])
            print('Name'+form.cleaned_data['email'])
            print('Name'+form.cleaned_data['text'])


    return render(request, 'first_app/form_page.html',{'form':form})

def home(request):
    return render(request, 'first_app/home.html')    
def register(request):

    registered = False

    if request.method == 'POST':

        # Get info from "both" forms
        # It appears as one form to the user on the .html page
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        # Check to see both forms are valid
        if user_form.is_valid() and profile_form.is_valid():

            # Save User Form to Database
            user = user_form.save()

            # Hash the password
            user.set_password(user.password)

            # Update with Hashed password
            user.save()

            # Now we deal with the extra info!

            # Can't commit yet because we still need to manipulate
            profile = profile_form.save(commit=False)

            # Set One to One relationship between
            # UserForm and UserProfileInfoForm
            profile.user = user

            # Check if they provided a profile picture
            if 'profile_pic' in request.FILES:
                print('found it')
                # If yes, then grab it from the POST form reply
                profile.profile_pic = request.FILES['profile_pic']

            # Now save model
            profile.save()

            # Registration Successful!
            registered = True

        else:
            # One of the forms was invalid if this else gets called.
            print(user_form.errors,profile_form.errors)

    else:
        # Was not an HTTP post so we just render the forms as blank.
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    # This is the render and context dictionary to feed
    # back to the registration.html file page.
    return render(request,'first_app/registration.html',
                          {'user_form':user_form,
                           'profile_form':profile_form,
                           'registered':registered})

