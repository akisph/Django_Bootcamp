from django.db import models
from django.utils import timezone
from django.urls import reverse # With this function we route the user after the entry of a comment or Post


# Create your models here.

class Post(models.Model):
    """ This is the model/table that contains the post in the blog """
    author = models.ForeignKey('auth.User',on_delete = models.CASCADE) # That is one way to pass a foreing key the current user
    title = models.CharField(max_length =  200)
    text = models.TextField()
    create_date =  models.DateTimeField(default = timezone.now()) 
    published_date = models.DateTimeField(blank=True,null=True) # Many post could created but not published so we don't have any publication

    def publish(self):
        """ Method to publish the post. That means to change/define the publication date """
        self.published_date = timezone.now() # change the publication date 
        self.save() # save the changes 
        
    def approve_comments(self):
        """ This method returns the approved comments """
        return self.comments.filter(approved_comment=True) # This filter and return only the approved comments
        #!!! The 'comments' here came from the foreign key related methods in Comment Class

    def get_absolute_url(self): # HAS TO GOT THAT NAME
        """ This function routes the user somewhere you want after the creation of a Post instance """
        return reverse('post_detail',  # the post_detail is a DetailView of the Post table
                        kwargs = {'pk':self.pk}) # this says that the primary key matches itself

    def __str__(self):
        return self.title


class Comment(models.Model): 
    """ This class create a table for the comments of the users """

    post =  models.ForeignKey('blog.Post',related_name='comments' ,on_delete = models.CASCADE) # Set foreign key to Post
    author = models.CharField(max_length = 200)
    text = models.TextField()
    create_date = models.DateTimeField(default = timezone.now()) 
    approved_comment = models.BooleanField(default=False) # this field show if the comment is approved

    def approve(self):
        """ Method to approve a comment """
        self.approved_comment = True
        self.save() 

    def get_absolute_url(self):
        """ This function routes the user somewhere you want after the creation of a Comment instance """
        return reverse('post_list') # retruns to the Home Page where in our case this is Post ListView

    def __str__(self):
        return self.text    
