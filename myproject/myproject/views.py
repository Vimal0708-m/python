#from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    #return HttpResponse("Welcome to the Home 
    # rPage!")
    details = {
        'title': 'Home Page',
        'content': 'Welcome to the Home Page!'
    }
    return render(request, 'home.html', details)

def about(request):
    #return HttpResponse("This is the About Page!")
    details = {
        'title': 'About Page',
        'content': 'This is the About Page!'
    }
    return render(request, 'about.html', details)
