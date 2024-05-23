from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),

    path('dom-active', views.dom_notif, name='notification'),

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

    # Process Language
    path('process-language', views.set_language, name='set_language'),
    path('process-chatbot-data', views.chatbot, name='chatbot'),
    path('reverse-geocoding-location', views.address_location, name='reverse-geocoding'),

    # news NEW FEATURE
    path('news', views.news, name='news'),
    path('delete-audio', views.delete_audio, name='delete_audio'),

    path('scrape', views.webscrape_news, name='scrape'),

]