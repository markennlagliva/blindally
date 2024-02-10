# Django Modules
from django.shortcuts import render
from django.utils import timezone
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Custom utils.py
from .utils import speak

# Files Manipulation 
import os
import json

# Home Page
@csrf_exempt
def index(request):
    if request.method == 'POST':
        # Status value here either T or F
        try:
            response = json.loads(request.body)
            print(f"This is the status value: {response.get('status')} and the data type: {type(response.get('status'))}" )
            speak(response.get('key'), response.get('details'), status=response.get('status')) # Differs in body key values
            return JsonResponse({'result': 'success', 'status': response.get('status')})

        except Exception as e:
            return JsonResponse({"status": False, "error":str(e)}, status=500)

    context = {}
    return render(request, 'base.html', context)

# Info apps pages
@csrf_exempt
def newsfeed(request):
    context = {}
    return render(request, 'partial/info-apps/_news.html', context)

@csrf_exempt
def current_time_date(request):
        
    current_datetime = timezone.now()
    print("Current date:", current_datetime.date())
    print("Current time:", current_datetime.time())
    formatted_time_12_hour = current_datetime.strftime("%I:%M %p")
    print(f'This is formatted time: {formatted_time_12_hour}')
    context = {}
    return render(request, 'partial/info-apps/_datetime.html', context)

@csrf_exempt
def location(request):
    context = {}
    return render(request, 'partial/info-apps/_location.html', context)

@csrf_exempt
def assistantbot(request):
    return render(request, 'partial/info-apps/_chatbot.html')

# Audio apps pages
@csrf_exempt
def audio_book(request):
    return render(request, 'partial/audio-apps/_book.html')

@csrf_exempt
def audio_music(request):
    return render(request, 'partial/audio-apps/_music.html')


# More pages
@csrf_exempt
def motivation(request):
    if request.method == 'POST':
        response = json.loads(request.body)
        speak(response.get('key'), response.get('details'), status=response.get('status')) # Differs in body key values
        return JsonResponse({'result': 'success', 'status': response.get('status')})

    
    context = {}
    return render(request, 'partial/more/_motivation.html', context)

@csrf_exempt
def technologies(request):
    if request.method == 'POST':
        response = json.loads(request.body)
        speak(response.get('key'), response.get('details'), status=response.get('status')) # Differs in body key values
        return JsonResponse({'result': 'success', 'status': response.get('status')})

    
    context = {}
    return render(request, 'partial/more/_technologies.html', context)

# About page
@csrf_exempt
def guidelines(request):
    return render(request, 'partial/_guidelines.html')

#added csrf_exempt for 403 forbidden request ERROR
