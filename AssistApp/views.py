from django.shortcuts import render

# Home Page
def index(request):
    context = {}
    return render(request, 'base.html', context)

# Info apps pages
def newsfeed(request):
    context = {}
    return render(request, 'partial/info-apps/_news.html', context)

def current_time_date(request):
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

    context = {}
    return render(request, 'partial/more/_motivation.html', context)

def technologies(request):

    context = {}
    return render(request, 'partial/more/_technologies.html', context)

# About page
def guidelines(request):
    return render(request, 'partial/_guidelines.html')