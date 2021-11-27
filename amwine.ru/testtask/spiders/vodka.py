import scrapy
from datetime import datetime as dt
from scrapy_splash import SplashRequest

class ViskiSpider(scrapy.Spider):
    name = 'vodka'
    allowed_domains = ['amwine.ru']
    start_urls = ['https://amwine.ru/catalog/krepkie_napitki/vodka/']
    pages_count = 20



    def parse(self, response):

        for page in range(1, 1 + self.pages_count):
            url = f"https://amwine.ru/catalog/krepkie_napitki/vodka/?page={page}"

            yield SplashRequest(url=url, callback=self.parse_page, dont_filter = True, args={
                            'wait': 2,
                            'html': 1
                        })

    def parse_page(self, response, **kwargs):

        for product in response.css('div.page-catalog-section'):
            link_to_product = product.css('div.catalog-list-item__container > a::attr(href)').get()
            yield SplashRequest(link_to_product, callback=self.parse_product)




    def parse_product(self, response, **kwargs):

            item = {
                "timestamp": dt.now().timestamp(),  # Текущее время в формате timestamp
                # "RPC": response.css('catalog-element-main > div:nth-child(2) > div > div.col-md-10.col-lg-6 > div > '
                #                     'div.catalog-element-info__sub > div.catalog-element-info__article >'
                #                     ' span::text').extract_first("").join(c for c in s if c.isdigit()),  # {str} Уникальный код товара
                "url": response.request.url,  # {str} Ссылка на страницу товара
                "title": f"{response.css('h1::text').get().replace(response.css('span.about-wine__param-value::text').get(),'')},{response.css('span.about-wine__param-value::text').get()}",

            }
            yield item