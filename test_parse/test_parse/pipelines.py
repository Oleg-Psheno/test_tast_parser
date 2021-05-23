# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import json

class TestParsePipeline:
    def process_item(self, item, spider):
        with open(f'test_parse/files/{item["id"][0]}.json','w', encoding='utf-8') as f:
            f.write(json.dumps(item,ensure_ascii=False))
        return item
