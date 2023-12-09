from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),

    # Info Apps
    path('newsfeed', views.newsfeed,  name='newsfeed'),
    path('current-time-date', views.current_time_date,  name='current_time_date'),
    path('location', views.location,  name='location'),
    path('assistant-bot', views.assistantbot,  name='assistantbot'),

    # Audio Apps
    path('audio-book', views.audio_book, name='audio_book'),
    path('audio-music', views.audio_music, name='audio_music'),

    # More
    path('motivation', views.motivation,  name='motivation'),
    path('technologies', views.technologies,  name='technologies'),

    # About 
    path('user-guidelines', views.guidelines,  name='guidelines'),



]