from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('newsfeed', views.newsfeed,  name='newsfeed'),
    path('current-time-date', views.current_time_date,  name='current_time_date'),
]