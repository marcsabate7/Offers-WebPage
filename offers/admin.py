from django.contrib import admin

from .models import Offer,Product,Company,Maker

admin.site.register(Offer)
admin.site.register(Product)
admin.site.register(Company)
admin.site.register(Maker)