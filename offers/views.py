from django.shortcuts import render,redirect
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .forms import CreateProduct,CreateOffer
from django.contrib import messages
from .models import Offer
from .models import Product
from .models import Company
from .models import Maker




def offers(request):
    #ofertas = Offer.objects.order_by('-offer_id')

    context = {"all_offers":Offer.objects.all()}
    return render(request,'offers/main.html',context)


def newEntities(request):

    return render(request,'offers/entities.html')


def createProduct(request):
    if request.method == 'POST':
        form = CreateProduct(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'The product has been created succesfully, now you can add an offer for this product!!')
            return redirect('offer-create')         
    else:
        form = CreateProduct()

    return render(request,'offers/product_form.html',{'form':form})



class ProductUpdateView(LoginRequiredMixin,UserPassesTestMixin, UpdateView):
    model = Product
    fields = ['id_product','product_name','category','description']


#####################################

class CompanyCreateView(LoginRequiredMixin, CreateView):
    model = Company
    fields = ['company_name','city','num_workers']


#####################################
class MakerCreateView(LoginRequiredMixin, CreateView):
    model = Maker
    fields = ['company_name','city','year_build']



#####################################

class OfferListView(ListView):
    model = Offer
    template_name = 'offers/main.html'
    context_object_name = 'all_offers'
    ordering = ['-offer_id']



class OfferCreateView(LoginRequiredMixin, CreateView):
    model = Offer
    template_name = 'offers/offer_form.html'
    form_class = CreateOffer


    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(OfferCreateView,self).form_valid(form)


class OfferDetailView(DetailView):
    model = Offer


class OfferUpdateView(LoginRequiredMixin,UserPassesTestMixin, UpdateView):
    model = Offer
    fields = ['offer_id','product_name','company_name','url_offer','new_price','old_price','discount','image']

    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        offer = self.get_object()
        if self.request.user == offer.author:
            return True
        return False

class OfferDeleteView(LoginRequiredMixin,UserPassesTestMixin, DeleteView):
    model = Offer
    success_url = '/'

    def test_func(self):
        offer = self.get_object()
        if self.request.user == offer.author:
            return True
        return False

