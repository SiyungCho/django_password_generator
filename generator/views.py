from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.

def home(request):
    return render(request, 'generator/home.html')

def password(request):
    Characters = 'abcdefghijklmnopqrstuvwxyz'
    if(request.GET.get('uppercase') == 'on'):
        Characters+='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    if(request.GET.get('special') == 'on'):
        Characters+="!@#$%^&*()'':;\.,<>/~+_=-"
    if(request.GET.get('numbers') == 'on'):
        Characters+="123456789"

    length = int(request.GET.get('length'))
    thepassword = ''

    for x in range (length):
        thepassword+=random.choice(Characters)
    
    return render(request, 'generator/password.html', {'password': thepassword})

def aboutme(request):
    return render(request, 'generator/aboutme.html')
