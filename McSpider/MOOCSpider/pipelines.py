# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem
class TextPipeline():
    def process_item(self, item, spider):
        if item['enrollCount']>10000:
            return item
        else:
            raise DropItem('Missing item')
import pymongo
class MongoPipeline():
    def __init__(self,mongo_uri,mongo_db):
        self.mongo_uri=mongo_uri
        self.mongo_db= mongo_db
    @classmethod#免除实例化
    def from_crawler(cls,crawler):
        return cls(
            mongo_uri=crawler.settings.get('MONGO_URL'),
            mongo_db =crawler.settings.get('MONGO_DB')
        )
    def open_spider(self,spider):
        self.client=pymongo.MongoClient(self.mongo_uri)
        self.db=self.client[self.mongo_db]
    def close_spider(self,spider):
        self.client.close()
    def process_item(self,item,spider):
        data={
            '课程名称': item['courseName'],
            '开课学校': item['university'],
            '课程类型': item['category'],
            '参与人数': item['enrollCount'],
            '课程概述': item['overview'],
            '授课目标':item['objective'],
            '预备知识':item['preliminaries'],
        }
        table=self.db['course']
        table.insert_one(data)
        return item