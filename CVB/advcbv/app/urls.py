from django.urls import path
from app import views


app_name = 'app'

urlpatterns=[
    path('',views.SchoolListViews.as_view(),name='list'),
    path('<int:pk>',views.SchoolDetailView.as_view(),name='detail')
]