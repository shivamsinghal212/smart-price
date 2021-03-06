from django.db import models


# Create your models here.

class ProductCatalogue(models.Model):
    name = models.CharField(max_length=300)
    vendor = models.CharField(max_length=50)
    url = models.URLField(max_length=500)
    image_url = models.URLField(max_length=1000)

    class Meta:
        db_table = 'product_catalogue'


class DailyProductData(models.Model):
    product = models.ForeignKey(ProductCatalogue, on_delete=models.CASCADE)
    datetime = models.DateTimeField(auto_now_add=True)
    price = models.FloatField(null=True)
    rating = models.FloatField(null=True)
    no_of_reviews = models.PositiveIntegerField(null=True)

    class Meta:
        db_table = 'daily_product_data'
