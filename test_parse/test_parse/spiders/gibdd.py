import scrapy
from ..loaders import GibddLoader


class GibddSpider(scrapy.Spider):
    name = 'gibdd'
    allowed_domains = ['https://xn--90adear.xn--p1ai/r/65/']
    start_urls = ['https://xn--90adear.xn--p1ai/news/region?perPage=20&page=1&region=65']
    headers = {'X-Requested-With': 'xmlhttprequest'}
    url = 'https://xn--90adear.xn--p1ai/news/region?perPage=20&page=1&region=65'
    params = {'perPage': '20',
              'page': '1',
              'region': '65'
              }


    def start_requests(self):

        yield scrapy.http.Request(self.url,method='GET',meta=self.params, headers=self.headers)

    def parse(self, response, *args, **kwargs):
        data = response.json()
        params = {
                  'perPage':'20',
                  'page': str(data['paginator']['page'] +1),
                  'region': '65',
                  }
        print(f'Обработка страницы {data["paginator"]["page"]}')
        for article in data['data']:
                id = article['id']
                url = f'https://xn--90adear.xn--p1ai/r/65/news/item/{id}?ajax=1'
                headers = {'X-Requested-With': 'xmlhttprequest',
                           'Referer':f'https://xn--90adear.xn--p1ai/r/65/news/item/{id}'}
                yield scrapy.http.Request(url, headers=headers,callback=self.parse_article, dont_filter=True)

        yield scrapy.FormRequest(self.url,callback=self.parse, method='GET',
                                 formdata=params, headers=self.headers, dont_filter=True)

    def parse_article(self,response):
        print(response.url)
        loader = GibddLoader(response=response)
        for k,v in response.json()['data'].items():
            loader.add_value(k,v)
        yield loader.load_item()



