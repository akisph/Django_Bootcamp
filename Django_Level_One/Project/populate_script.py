import os 


os.environ['DJANGO_SETTINGS_MODULE'] = 'Project.settings' # Configuring the settings for the project 
import django
django.setup()

import random 
from app.models import User
from faker import Faker

fakegen = Faker()
def populate(N=5):
    
    for entry in range(N):
        first_name = fakegen.first_name()
        last_name = fakegen.last_name()
        email = fakegen.email()

        user = User.objects.get_or_create(first_name=first_name,
                                          last_name=last_name,
                                          email = email )

if __name__=='__main__':
    
    
    print('Population Script')
    populate(40)
    print('Populate Completed')