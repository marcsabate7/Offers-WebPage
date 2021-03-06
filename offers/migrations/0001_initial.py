# Generated by Django 3.1.6 on 2021-05-01 16:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('num_workers', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Maker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('year_build', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id_product', models.AutoField(primary_key=True, serialize=False)),
                ('product_name', models.CharField(max_length=100)),
                ('category', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('date_posted', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('offer_id', models.AutoField(primary_key=True, serialize=False)),
                ('new_price', models.IntegerField()),
                ('old_price', models.IntegerField()),
                ('discount', models.IntegerField()),
                ('company_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='offers.maker')),
                ('product_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='offers.product')),
            ],
        ),
    ]
