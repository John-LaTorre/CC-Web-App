## Defines URL patterns for LearningLog

from django.urls import path


from . import views

urlpatterns = [
    #Home page
    path('', views.index),
    
    
]
