from data_collection.scrapers.flipkart import ProductScrapper
from data_collection.models import ProductCatalogue, DailyProductData
from datetime import datetime


class Populator:
    def __init__(self, url):
        self.url = url
        self.scrapper_obj = ProductScrapper(self.url)

    def _validate_url(self):
        return True

    def get_scraped_data(self):
        if self._validate_url():
            self.scrapper_obj.initialize()
            product_data = self.scrapper_obj.get_product_data()
            return product_data
        else:
            return None

    def update_product_catalogue(self, data=None, update_daily=False):
        if data:
            pc_obj = ProductCatalogue.objects.filter(url=data['url']).first()
            if not pc_obj:
                pc_obj = ProductCatalogue.objects.create(url=self.url, name=data['name'], image_url='www.google.com',
                                                         vendor='FK')
            if update_daily:
                self.update_daily_data(pc_obj, data)
            return pc_obj

    def update_daily_data(self, pc_obj: ProductCatalogue, product_data):
        current_date = datetime.now().date()
        if product_data:
            dpd_obj: DailyProductData = DailyProductData.objects.filter(product=pc_obj, datetime__day=current_date.day,
                                                                        datetime__month=current_date.month,
                                                                        datetime__year=current_date.year).first()
            if dpd_obj:
                dpd_obj.rating = product_data['rating']
                dpd_obj.price = product_data['price']
                dpd_obj.no_of_reviews = product_data['no_of_reviews']
                dpd_obj.save()
            else:
                DailyProductData.objects.create(product=pc_obj, price=product_data['price'],
                                                rating=product_data['rating'],
                                                no_of_reviews=product_data['no_of_reviews'])

    def populate(self):
        data = self.get_scraped_data()
        self.update_product_catalogue(data, update_daily=True)
        print(data)
        return data
