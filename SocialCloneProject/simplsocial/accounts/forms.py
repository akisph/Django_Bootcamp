from django.contrib.auth import get_user_model # get the user model that is currently active for this model
from django.contrib.auth.forms import UserCreationForm # Built-in from for User Creation

class UserCreateForm(UserCreationForm): 

    class Meta:
        fields = ('username','email','password1','password2')
        model = get_user_model() # Better take the model like this. Not by assign

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        # This is a way to add label in the form 
        self.fields['username'].label = 'Display Name' #!!!
        self.fields['email'].label = 'Email Address'
        self.fields['password1'].label = 'Password'
        self.fields['password2'].label = 'Validate Password' # Dummy name just to check what it changes