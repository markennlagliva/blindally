# Django Modules
from django.shortcuts import render
from django.utils import timezone
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Custom utils.py
from .utils import speak
from .utils import AudioApps
import datetime

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
            print(type(response.get('details')), response.get('details'))
            # print(f"This is the status value: {response.get('status')} and the data type: {type(response.get('status'))}" )
            speak(response.get('details'), status=response.get('status')) # Differs in body key values
            return JsonResponse({'result': 'success', 'status': response.get('status')})

        except Exception as e:
            return JsonResponse({"error":str(e)})

    context = {}
    return render(request, 'base.html', context)

# Info apps pages
@csrf_exempt
def newsfeed(request):
    if request.method == 'POST':
        # Status value here either T or F
        try:
            response = json.loads(request.body)
            print(type(response.get('details')), response.get('details'))
            # print(f"This is the status value: {response.get('status')} and the data type: {type(response.get('status'))}" )
            speak(response.get('details'), status=response.get('status')) # Differs in body key values
            return JsonResponse({'result': 'success', 'status': response.get('status')})

        except Exception as e:
            return JsonResponse({"error":str(e)})
    current_datetime = datetime.datetime.now()
    date_readable_format = current_datetime.strftime("%B %d, %Y")
    day_of_week = current_datetime.strftime("%A")

    from datetime import time
    # Specify the time to compare (4:00 PM or 16:00)
    compare_time = time(16, 0)  # 4:00 PM

    # Compare the current time with the specified time
    if current_datetime.time() < compare_time:
        formatted_time = "4AM"
    else:
        formatted_time = "4PM"


    context = {'date': date_readable_format, 'day': day_of_week, 'time': formatted_time}
    return render(request, 'partial/info-apps/_news.html', context)

@csrf_exempt
def current_time_date(request):
    current_datetime = datetime.datetime.now()
    # Format the time in 12-hour format
    time_12_format = current_datetime.strftime("%I:%M %p")
    # Format the date in a more readable format
    date_readable_format = current_datetime.strftime("%B %d, %Y")
    if request.method == 'POST':
        try:
            response = json.loads(request.body)
            print(response.get('details'))
            speak(details=response.get('details'), status=response.get('status'))

            return JsonResponse({'result': 'success'})
        except Exception as e:
            print(str(e))
            return JsonResponse({'Error': str(e)})

    # Get current date and time
    

    context = {'time': time_12_format, 'date': date_readable_format}
    return render(request, 'partial/info-apps/_datetime.html', context)

@csrf_exempt
def location(request):
    context = {}
    if request.method == 'POST':
        try:
            response = json.loads(request.body)

            speak(details=response.get('details'), status=response.get('status'))

            return JsonResponse({'result': 'success'})
        except Exception as e:
            print(str(e))
            return JsonResponse({'Error': str(e)})


    return render(request, 'partial/info-apps/_location.html', context)

@csrf_exempt
def assistantbot(request):

    if request.method == 'POST':
        try:
            response = json.loads(request.body)

            speak(details=response.get('details'), status=response.get('status'))

            return JsonResponse({'result': 'success'})
        except Exception as e:
            print(str(e))
            return JsonResponse({'Error': str(e)})


    return render(request, 'partial/info-apps/_chatbot.html')

# Audio apps pages
@csrf_exempt
def audio_book(request):

    if request.method == 'POST':
        try:
            response = json.loads(request.body)

            audioBook = AudioApps()
            token = audioBook.get_token()

            speak(details=response.get('details'), status=response.get('status'))

            return JsonResponse({'result': 'success'})
        except Exception as e:
            print(str(e))
            return JsonResponse({'Error': str(e)})

    return render(request, 'partial/audio-apps/_book.html')

@csrf_exempt
def audio_music(request):
    if request.method == 'POST':
        try:
            response = json.loads(request.body)

            audioBook = AudioApps()
            token = audioBook.get_token()
            
                
            speak(details=response.get('details'), status=response.get('status'))

            return JsonResponse({'result': 'success'})
        except Exception as e:
            print(str(e))
            return JsonResponse({'Error': str(e)})

    return render(request, 'partial/audio-apps/_music.html')


# More pages
@csrf_exempt
def motivation(request):
    if request.method == 'POST':
        response = json.loads(request.body)
        speak(response.get('details'), status=response.get('status')) # Differs in body key values
        return JsonResponse({'result': 'success', 'status': response.get('status')})

    
    context = {}
    return render(request, 'partial/more/_motivation.html', context)

@csrf_exempt
def technologies(request):
    if request.method == 'POST':
        response = json.loads(request.body)
        speak(response.get('details'), status=response.get('status')) # Differs in body key values
        return JsonResponse({'result': 'success', 'status': response.get('status')})

    
    context = {}
    return render(request, 'partial/more/_technologies.html', context)

# About page
@csrf_exempt
def guidelines(request):

    if request.method == 'POST':
        try:
            response = json.loads(request.body)
            speak(response.get('details'), response.get('status'))

            return JsonResponse({'result': 'success', 'status': response.get('status')})
        except Exception as e:
            return JsonResponse({"error":str(e)})
        
    return render(request, 'partial/_guidelines.html')

#added csrf_exempt for 403 forbidden request ERROR
@csrf_exempt
def set_language(request):
    if request.method == 'POST':
        try:
            response = json.loads(request.body)
            speak(response.get('details'), response.get('status'))

            return JsonResponse({'result': 'success', 'status': response.get('status')})
        except Exception as e:
            return JsonResponse({"error":str(e)})
        
@csrf_exempt
def chatbot(request):
    if request.method == 'POST':
        try:
            import openai
            from dotenv import load_dotenv
            load_dotenv()
            openai.api_key = os.getenv('OPENAI_KEY_3')
            response = json.loads(request.body)
            
            completion = openai.ChatCompletion.create(
                model='gpt-3.5-turbo',
                messages=[
                    {
                    "role": "user", 
                    #This is Where USER DATA REQUEST will be process.
                    "content": response.get('details')
                    },
                ]
            )
            
            return JsonResponse({'result': 'success', 'generatedText': completion['choices'][0]['message']['content']})
        except Exception as e:
            print(str(e))
            return JsonResponse({'Error': str(e)})
    