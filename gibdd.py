import scrapy


class GibddSpider(scrapy.Spider):
    name = 'gibdd'
    allowed_domains = ['https://xn--90adear.xn--p1ai/r/65/']
    start_urls = ['http://https://xn--90adear.xn--p1ai/r/65//']

    def parse(self, response):
        pass
