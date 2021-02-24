from django.db import models

from django.contrib.auth.models import User
# Create your models here.
class Topic(models.Model):
    # This is the base class for the xample #
    top_name = models.CharField(max_length=264,unique=True)

    def __str__(self):
        return self.top_name

class Webpage(models.Model):

    """ The class define the first table of the database """

    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    name = models.CharField(max_length = 264 , unique = True)
    url = models.URLField(unique=True)

    def __str__(self):
        return self.name 


class AccessRecord(models.Model):
    name = models.ForeignKey(Webpage,on_delete=models.CASCADE)
    date = models.DateField()


    def __str__(self):
        return str(self.date)


class UserProfileInfo(models.Model):

    """ This model extends the user model to 
    have also portfolio url and a profile picture """


    user = models.OneToOneField(User,on_delete=models.CASCADE) # create realitotinship NOT Inheritance

    # additional attributes
    portfolio = models.URLField(blank = True) # blank = True : means the user doesnt need filled out
    picture = models.ImageField( upload_to = 'profile_pics', # define where we need to upload the picture to 
                                 blank = True) 

    def __str__(self):
        return self.user.username



