from django.shortcuts import render
from django.http import HttpResponse



def offers(request):
    return HttpResponse('<h1>OFFERS PAGE</h1>')

