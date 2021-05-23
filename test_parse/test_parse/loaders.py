from scrapy.loader import ItemLoader


class GibddLoader(ItemLoader):
    default_item_class = dict
