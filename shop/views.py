
import requests
from django.http import HttpResponse
from django.http import HttpResponseRedirect

def greetings(requests):
    return HttpResponse('Добро пожаловать в наш магазин!')

def cats(requests):
    API = 'https://catfact.ninja/fact'
    return HttpResponseRedirect(API)