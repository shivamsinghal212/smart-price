# Generated by Django 3.1.1 on 2020-09-30 21:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data_collection', '0002_auto_20201001_0053'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='dailyproductdata',
            table='daily_product_data',
        ),
        migrations.AlterModelTable(
            name='productcatalogue',
            table='product_catalogue',
        ),
    ]