from django.shortcuts import render
from django.http import HttpResponse



def offers(request):
    return render(request,'offers/main.html',{'title':'Home'})
