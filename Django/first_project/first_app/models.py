from django.db import models

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


