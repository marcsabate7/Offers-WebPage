# Generated by Django 3.1.6 on 2021-05-06 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('offers', '0008_auto_20210503_2010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offer',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='offers'),
        ),
        migrations.AlterField(
            model_name='offer',
            name='url_offer',
            field=models.URLField(default='', max_length=250),
        ),
    ]
