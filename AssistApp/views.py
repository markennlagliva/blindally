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

# Reading .mp3 files
from playsound import playsound

# Scraping
import requests
from bs4 import BeautifulSoup
import random
from gtts import gTTS
from googletrans import Translator

# Home Page
@csrf_exempt
def index(request):
    # playsound('audio/notif.mp3')
    if request.method == 'POST':
        # Status value here either T or F
        try:
            response = json.loads(request.body)

            if response.get('details') == 'shutdown':
                os.system("shutdown /s /t 1")
            elif response.get('details') == 'secret activation':
                os.system('shutdown /r /t 1') 
            
            print(type(response.get('details')), response.get('details'))
            # print(f"This is the status value: {response.get('status')} and the data type: {type(response.get('status'))}" )
            speak(response.get('details'), status=response.get('status')) # Differs in body key values
            return JsonResponse({'result': 'success', 'status': response.get('status')})

        except Exception as e:
            return JsonResponse({"error":str(e)})

    context = {}
    return render(request, 'base.html', context)

@csrf_exempt
def dom_notif(request):
    if request.method == 'POST':
        try:
            response = json.loads(request.body)
            speak(response.get('details'), status=response.get('status')) # Differs in body key values
            return JsonResponse({'result': 'success', 'status': response.get('status')})

        except Exception as e:
            return JsonResponse({"error":str(e)})


# Info apps pages
@csrf_exempt
def newsfeed(request):
    if request.method == 'POST':
        # Status value here either T or F
        try:
            response = json.loads(request.body)
            if response.get('details') == 'restart':
                os.system('shutdown /r /t 1')   
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
            # import openai
            # from dotenv import load_dotenv
            # load_dotenv()
            # openai.api_key = os.getenv('OPENAI_KEY_3')
            response = json.loads(request.body)
            
            # completion = openai.ChatCompletion.create(
            #     model='gpt-3.5-turbo',
            #     messages=[
            #         {
            #         "role": "user", 
            #         #This is Where USER DATA REQUEST will be process.
            #         "content": response.get('details')
            #         },
            #     ]
            # )
            
            # return JsonResponse({'result': 'success', 'generatedText': completion['choices'][0]['message']['content']})
            from g4f.client import Client
            client = Client()

            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {
                        "role": "user",
                        "content": response.get('details') + ' English response only and Summarize, maximum of 4000 or less than 4000 characters only. Only characters or numbers response only.',
                    },
                ]
            )

            return JsonResponse({'result': 'success', 'generatedText': response.choices[0].message.content})
        except Exception as e:
            print(str(e))
            return JsonResponse({'Error': str(e)})

@csrf_exempt
def address_location(request):
    if request.method == 'POST':
        try:
            from geopy.geocoders import Nominatim

            geoLoc = Nominatim(user_agent="GetLoc")

            response = json.loads(request.body)
            locname = geoLoc.reverse(f"{response.get('lat')}, {response.get('long')}")
            # Extract area and country
            address = locname.raw['address']
            anemity = address.get('amenity', '') if address.get('amenity', '') else ''
            area = address.get('quarter', '') if address.get('quarter', '') else ''
            town = address.get('town', '') if address.get('town', '') else ''
            state = address.get('state', '') if address.get('state', '') else ''
            region = address.get('region', '') if address.get('region', '') else ''
            country = address.get('country', '') if address.get('country', '') else ''
            loc = [anemity, area, town, state, region, country]

            full_loc = []
            for l in loc:
                if l:
                    full_loc.append(l)            

            return JsonResponse({'result': 'success', 'address': ', '.join(full_loc)})
        except Exception as e:
            return JsonResponse({"error":str(e)})


@csrf_exempt
def news(request):
    if request.method == 'POST':
        try:
            response = json.loads(request.body)
            output, status = response.get('details'), response.get('status')
            response = requests.get(f'https://newsapi.org/v2/everything?q={output}&apiKey=e4ab186e11c44ce98d27149a279b3ef9')
            data = response.json()
            # print(data['totalResults'], type(data['totalResults']))
            content_web = []
            hasNews = data['totalResults'] > 0
            if hasNews:
                # Generate a random integer between 1 and 10 (inclusive)
                random_integer = random.randint(1, 5)
                url = data['articles'][random_integer]['url']

                # print(title)
                # print(url)
                # print(content)
                # if content is None:
                # Get information on URL website

                # Step 2: Fetch the webpage content
                response = requests.get(url)
                webpage_content = response.text

                # Step 3: Parse the HTML content
                soup = BeautifulSoup(webpage_content, 'html.parser')

                # Step 4: Extract all <p> tags
                p_tags = soup.find_all('p', limit=5)

                # Step 5: Process the extracted <p> tags
                
                for p in p_tags:
                    content_web.append(p.get_text())
                # else:
                #     content_web.append(content)

                # audio = gTTS(' '.join(content_web), lang='en', slow=False)
                if status: #Fil
                    audio = gTTS(' '.join(content_web), lang='en', slow=False)
                else:
                    result = Translator().translate(' '.join(content_web), dest='tl')
                    audio = gTTS(result.text, lang='tl', slow=False)
                audio.save('static/audio/newssound.mp3')
            else:
                speak('Sorry no news found, Try finding another news!', status)
            
            print(' '.join(content_web))
            # speak(' '.join(content_web), status)



            return JsonResponse({'result': 'success', 'status': data, 'titleNews': data['articles'][random_integer]['title'], 'content_web': content_web, 'hasNews': hasNews, 'urlToImage': data['articles'][random_integer]['urlToImage']})
        except Exception as e:
            return JsonResponse({"error":str(e)})

@csrf_exempt
def delete_audio(request):
    if request.method == 'POST':
        os.remove('static/audio/newssound.mp3')

    return JsonResponse({'result': 'success'})

@csrf_exempt
def webscrape_news(request):
    if request.method == 'POST':
        try:

            response = json.loads(request.body)
            output, status = response.get('details'), response.get('status')
            url = "https://real-time-news-data.p.rapidapi.com/search"

            querystring = {"query": response.get('deetails'),"country":"US","lang":"en"}

            headers = {
                "X-RapidAPI-Key": "1cb3bdc85emsh88a3549de3600d6p1ffddcjsn92e56802c9d2",
                "X-RapidAPI-Host": "real-time-news-data.p.rapidapi.com"
            }

            data = requests.get(url, headers=headers, params=querystring)
            speak(f'Scraping the whole news, please wait for a moment ', status)
            print(data)

            # Step 2: Fetch the webpage content
            response = requests.get(data['data'][0]['link']) # Details as URL
            webpage_content = response.text

            # Step 3: Parse the HTML content
            soup = BeautifulSoup(webpage_content, 'html.parser')

            # Step 4: Extract all <p> tags
            p_tags = soup.find_all('p')

            # Step 5: Process the extracted <p> tags
            content_web = []
            for p in p_tags[:4]:
                content_web.append(p.get_text())
            # else:
            #     content_web.append(content)
            from gtts import gTTS
            print(response.get('status'))
            if status: #Fil
                audio = gTTS(' '.join(content_web), lang='en', slow=False)
            else:
                audio = gTTS(' '.join(content_web), lang='tl', slow=False)
                
            audio.save('static/audio/newssound.mp3')
            
            print(' '.join(content_web))
            # speak(' '.join(content_web), status)



            return JsonResponse({'result': 'success', 'content_web': content_web})
        except Exception as e:
            return JsonResponse({"error":str(e)})