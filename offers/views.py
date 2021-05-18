from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView
from django.http import HttpResponse

from .models import Offer
from .models import Product
#from .models import Company
#from .models import Maker

def offers(request):
    #ofertas = Offer.objects.order_by('-offer_id')

    context = {"all_offers":Product.objects.all()}
    return render(request,'offers/main.html',context)


class OfferListView(ListView):
    model = Product
    template_name = 'offers/main.html'
    context_object_name = 'all_offers'
    ordering = ['-id_product']

class OfferDetailView(DetailView):
    model = Product

class OfferCreateView(CreateView):
    model = Product
    fields = ['id_product','product_name','category','description']