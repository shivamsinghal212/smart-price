from data_collection.models import ProductCatalogue
from data_collection.services.populator import Populator


def update_daily_data():
    all_product_urls = ProductCatalogue.objects.filter().values_list('url', flat=True)
    for url in all_product_urls:
        print('updating: ', url)
        Populator(url).populate()
