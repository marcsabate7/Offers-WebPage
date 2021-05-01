from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Product(models.Model):
    id_product = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    description = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

class Company(models.Model):
    company_name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    num_workers = models.IntegerField()
    
class Maker(models.Model):
    company_name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    year_build = models.IntegerField()

class Offer(models.Model):
    offer_id = models.AutoField(primary_key=True)
    product_name = models.ForeignKey(Product, on_delete=models.CASCADE)
    company_name = models.ForeignKey(Company, on_delete=models.CASCADE)
    company_name = models.ForeignKey(Maker, on_delete=models.CASCADE)
    new_price = models.IntegerField()
    old_price = models.IntegerField()
    discount = models.IntegerField()
