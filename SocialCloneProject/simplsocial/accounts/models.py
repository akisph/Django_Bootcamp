from django.db import models
from django.contrib import auth #For Authorization
# Create your models here.

class User(auth.models.User, auth.models.PermissionsMixin):
    #!!! Check auth.model.User Model. 
    """ A user model """

    def __str__(self):
        return "@{}".format(self.username)