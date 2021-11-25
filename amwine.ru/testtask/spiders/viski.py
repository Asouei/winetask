import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class ViskiSpider(scrapy.Spider):
    name = 'viski'
    allowed_domains = ['https://amwine.ru/catalog/krepkie_napitki/viski/']
    start_urls = ['http://https://amwine.ru/catalog/krepkie_napitki/viski//']

    def parse(self, response):
        pass
