#Mindgram views

#Django
from django.http import HttpResponse

#Utilities
from datetime import datetime
import json

def hello_world(request):
    return HttpResponse('Hi! Current server time is {now})'.format(
        now=datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
    ))

def say_hi(request, name, age):
    if age < 12:
        message = 'Sorry {}, you are not allowed here'.format(name)
    else:
        message = 'Hi, {}! Welcome to Mindgram'.format(name)

    return HttpResponse(message)