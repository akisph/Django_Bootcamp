from django.shortcuts import render
from django.views.generic import View,TemplateView,ListView,DetailView
from django.http import HttpResponse
from app.models import School,Student


class IndexView(TemplateView):
    template_name = 'index.html'

    # def get_context_data(self,**kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['injectme'] = 'DATA_INJECTED'
    #     return context



class SchoolListViews(ListView):
    """ Provide by a list of every record of this model """
    model = School 
    """ This automatically returns the input fro the html as loewer(<model_name>)+'_list' 
    in our case: school_list """
    # if we want to change that we define 
    # context_object_name = 'schools' 
    # and that wil return to html a variable named schools

    


class SchoolDetailView(DetailView):
    """ Give all the details of a model 
        .... theese means that in this example will also show every 
            every student of each school """
    context_object_name = 'school_detail'
    model = School
    template_name = 'app/school_detail.html'


  