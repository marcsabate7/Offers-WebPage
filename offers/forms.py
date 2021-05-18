from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Product,Offer



class CreateProduct(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['id_product','product_name','category','description']



class CreateOffer(forms.ModelForm):
    class Meta:
        model = Offer
        fields = ['offer_id','product_name','company_name','address','url_offer','new_price','old_price','discount','image']
