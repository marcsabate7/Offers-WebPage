# Generated by Django 3.1.6 on 2021-05-03 17:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('offers', '0005_auto_20210503_1859'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offer',
            name='product_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='offers.product'),
        ),
    ]
