# Generated by Django 3.1.6 on 2021-05-12 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('offers', '0014_auto_20210512_1116'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offer',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='offers'),
        ),
    ]