from django.shortcuts import render

# Create your views here.
def index(request):

    context = {}
    return render(request, 'base.html', context)

def newsfeed(request):

    context = {}
    return render(request, 'partial/_news.html', context)

def current_time_date(request):

    context = {}
    return render(request, 'partial/_datetime.html', context)


def location(request):

    context = {}
    return render(request, 'partial/_location.html', context)