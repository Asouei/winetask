import scrapy
from datetime import datetime as dt
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class ViskiSpider(scrapy.Spider):
    name = 'viski'
    allowed_domains = ['amwine.ru']
    start_urls = ['http://https://amwine.ru/catalog/krepkie_napitki/viski//']
    pages_count = 20

    def start_requests(self):
        for page in range(1, 1 + self.pages_count):
            url = f"https://amwine.ru/catalog/krepkie_napitki/vodka/?page={page}"
            yield scrapy.Request(url, callback=self.parse_pages)

    def parse_pages(self, response, **kwargs):
        for href in response.css('#section-container > div.catalog-section-itemlist.parent-selector.js-catalog-section-items > div:nth-child(2) >'
                                 ' div.catalog-list-item__container > div.catalog-list-item__info > a::attr("href")').extract():
            url = response.urljoin(href)
            print(f"!!!!!!!!!! ----    {url}")
            yield scrapy.Request(url, callback=self.parse)

    def parse(self, response, **kwargs):
        item = {
        "timestamp":dt.now().timestamp(), # Текущее время в формате timestamp
        "RPC": response.css('#catalog-element-main > div:nth-child(2) > div > div.col-md-10.col-lg-6 > div > '
                            'div.catalog-element-info__sub > div.catalog-element-info__article >'
                            ' span::text').extract_first("").join(c for c in s if c.isdigit()),  # {str} Уникальный код товара
        # "url": response.request.url,  # {str} Ссылка на страницу товара
        # "title": "",  # {str} Заголовок/название товара (если в карточке товара указан цвет или объем, необходимо добавить их в title в формате: "{название}, {цвет}")
        # "marketing_tags": [],  # {list of str} Список тэгов, например: ['Популярный', 'Акция', 'Подарок'], если тэг представлен в виде изображения собирать его не нужно
        # "brand": "",  # {str} Брэнд товара
        # "section": [],  # {list of str} Иерархия разделов, например: ['Игрушки', 'Развивающие и интерактивные игрушки', 'Интерактивные игрушки']
        # "price_data": {
        #     "current": 0.,  # {float} Цена со скидкой, если скидки нет то = original
        #     "original": 0.,  # {float} Оригинальная цена
        #     "sale_tag": ""  #{str} Если есть скидка на товар то необходимо вычислить процент скидки и записать формате: "Скидка {}%"
        # },
        # "stock": {
        #     "in_stock": True,  # {bool} Должно отражать наличие товара в магазине
        #     "count": 0 # {int} Если есть возможность получить информацию о количестве оставшегося товара в наличии, иначе 0
        # },
        # "assets": {
        #     "main_image": "",  # {str} Ссылка на основное изображение товара
        #     "set_images": [],  # {list of str} Список больших изображений товара
        #     "view360": [],  # {list of str}
        #     "video": []  # {list of str}
        # },
        # "metadata": {
        #     "__description": "",  # {str} Описание товар
        #     # Ниже добавить все характеристики которые могут быть на странице тоавара, такие как Артикул, Код товара, Цвет, Объем, Страна производитель и т.д.
        #     "АРТИКУЛ": "A88834",
        #     "СТРАНА ПРОИЗВОДИТЕЛЬ": "Китай"
        # }
        # "variants": 1,  # {int} Кол-во вариантов у товара в карточке (За вариант считать только цвет или объем/масса. Размер у одежды или обуви варинтами не считаются)
        }
        yield item

