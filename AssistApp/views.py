# Django Modules
from django.shortcuts import render
from django.utils import timezone
from django.http import JsonResponse

# Custom utils.py
from .utils import speak

# Files Manipulation 
import os
import json

# Home Page
def index(request):
    if request.method == 'POST':
        # Status value here either T or F
        response = json.loads(request.body)
        print(f"This is the status value: {response.get('status')} and the data type: {type(response.get('status'))}" )
        speak(response.get('key'), response.get('details'), status=response.get('status')) # Differs in body key values
        return JsonResponse({'result': 'success', 'status': response.get('status')})

    context = {}
    return render(request, 'base.html', context)

# Info apps pages
def newsfeed(request):
    context = {}
    return render(request, 'partial/info-apps/_news.html', context)

def current_time_date(request):
        
    current_datetime = timezone.now()
    print("Current date:", current_datetime.date())
    print("Current time:", current_datetime.time())
    formatted_time_12_hour = current_datetime.strftime("%I:%M %p")
    print(f'This is formatted time: {formatted_time_12_hour}')
    context = {}
    return render(request, 'partial/info-apps/_datetime.html', context)

def location(request):
    context = {}
    return render(request, 'partial/info-apps/_location.html', context)

def assistantbot(request):
    return render(request, 'partial/info-apps/_chatbot.html')

# Audio apps pages
def audio_book(request):
    return render(request, 'partial/audio-apps/_book.html')

def audio_music(request):
    return render(request, 'partial/audio-apps/_music.html')


# More pages
def motivation(request):
    if request.method == 'POST':
        response = json.loads(request.body)
        speak(response.get('key'), response.get('details'), status=response.get('status')) # Differs in body key values
        return JsonResponse({'result': 'success', 'status': response.get('status')})

    
    context = {}
    return render(request, 'partial/more/_motivation.html', context)

def technologies(request):
    if request.method == 'POST':
        response = json.loads(request.body)
        speak(response.get('key'), response.get('details'), status=response.get('status')) # Differs in body key values
        return JsonResponse({'result': 'success', 'status': response.get('status')})

    
    context = {}
    return render(request, 'partial/more/_technologies.html', context)

# About page
def guidelines(request):
    return render(request, 'partial/_guidelines.html')

