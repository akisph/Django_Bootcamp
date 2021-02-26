# Here are the projects view where we can keep the views for the home page etc
from django.views.generic import TemplateView

class HomePage(TemplateView):
    template_name = 'index.html'