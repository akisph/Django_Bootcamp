import os 


os.environ['DJANGO_SETTINGS_MODULE'] = 'first_project.settings' # Configuring the settings for the project 
import django
django.setup()

## Fake population scripts
import random 
from first_app.models import AccessRecord,Webpage,Topic
from faker import Faker

fakegen = Faker()
topics = ['Search','Social','Marketplace','News','Games']

def add_topic():
    t = Topic.objects.get_or_create(top_name = random.choice(topics))[0]# this either get the object if exists or create it if not
    t.save()
    return t

def populate(N=5):

    for entry in range(N):

        top = add_topic()

        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.company()

        # new fake webpage 
        webpg = Webpage.objects.get_or_create(topic = top, url=fake_url,name=fake_name)[0]

        # create fake access
        acc_rec = AccessRecord.objects.get_or_create(name=webpg, date=fake_date)[0]

if __name__=='__main__':

    
    print('Population Script')
    populate(20)
    print('Populate Completed')