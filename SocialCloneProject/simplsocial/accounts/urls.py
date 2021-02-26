from django.urls import path
from django.contrib.auth import views as auth_views #so we don't think it is our views
from . import views

app_name = 'accounts'

urlpatterns = [
    path('login/',auth_views.LoginView.as_view(template_name='accounts/login.html'),name='login'), # The login view you have to connect it to the template
    path('logout/',auth_views.LogoutView.as_view(),name='logout'), # This one has a default view that we are going to use
    path('signup/',views.SignUp.as_view(),name='signup'),
]