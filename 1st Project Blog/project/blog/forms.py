# We created this file 
# To handle the form / input to the tables

from django import forms
from blog.models import Post,Comment


class PostForm(forms.ModelForm):
    """ This class define the form for the post """

    class Meta:
        model  = Post #connect to Post Model
        fields = ('author','title','text') 

        # Edit the widgets
        # SOS
        widgets = {
            'title':forms.TextInput(attrs={'class':'textinputClass'}), # as atttributes pass the actual HTML attributes want to have
            'text' : forms. Textarea(attrs = {'class':'editable medium-editor-textarea postcontentent'}) # In example here we pass some bootstrap classes

        }


class CommentForm(forms.ModelForm):
    """ This class define the form for the comment """

    class Meta:
        model = Comment
        fields = ('author','text')        

        # Edit the widgets 
        widgets = {
            'author': forms.TextInput(attrs={'class':'textinputClass'}),
            'text' : forms. Textarea(attrs = {'class':'editable medium-editor-textarea commentcontent'})
        }
        

