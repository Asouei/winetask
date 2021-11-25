import scrapy


class VodkaSpider(scrapy.Spider):
    name = 'vodka'
    allowed_domains = ['https://amwine.ru/catalog/krepkie_napitki/vodka/']
    start_urls = ['http://https://amwine.ru/catalog/krepkie_napitki/vodka//']

    def parse(self, response):
        pass
