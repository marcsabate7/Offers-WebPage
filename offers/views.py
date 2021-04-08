from django.shortcuts import render
from django.http import HttpResponse

from .models import Offer

def offers(request):
    ofertas = Offer.objects.order_by('-offer_id')

    context = {"all_offers":ofertas}
    return render(request,'offers/main.html',context)
