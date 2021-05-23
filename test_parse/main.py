from scrapy.crawler import CrawlerProcess
from scrapy.settings import Settings
from test_parse.spiders.gibdd import GibddSpider

if __name__ == '__main__':
    crawler_settings = Settings()
    crawler_settings.setmodule('test_parse.settings')
    crawler_process = CrawlerProcess(settings=crawler_settings)
    crawler_process.crawl(GibddSpider)
    crawler_process.start()


