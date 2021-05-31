from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils import timezone
from django.conf import settings
from PIL import Image

class Product(models.Model):
    id_product = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return u"%s" % self.product_name

class Company(models.Model):
    company_name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    num_workers = models.IntegerField()

    def __str__(self):
        return self.company_name
    
class Maker(models.Model):
    company_name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    year_build = models.IntegerField()

class Offer(models.Model):
    offer_id = models.AutoField(primary_key=True)
    product_name = models.ForeignKey(Product,on_delete=models.CASCADE)
    company_name = models.CharField(max_length=100)
    sku = models.CharField(max_length=10, default='')
    new_price = models.IntegerField()
    old_price = models.IntegerField()
    discount = models.IntegerField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User,default=1,on_delete=models.CASCADE)
    url_offer = models.URLField(max_length=250,default="",help_text="*In case the offer is local put the shop website URL")
    address = models.CharField(max_length=1000,blank=True,help_text="*Add address in case the offer is in a local site")
    image = models.ImageField(default='default.jpg',upload_to='offers')


    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)
        img.save(self.image.path)

    def __str__(self):
        return u"%s" % self.product_name

    def get_absolute_url(self):
        return reverse('offer-detail',kwargs={'pk':self.pk})