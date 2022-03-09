from redis import Redis
import json


class FeedPipeline:
    """
    Предоставляет pipeline для обмена данными spiders через redis.
    """
    def __init__(self, connection_string):
        if connection_string:
            self.connection_string = connection_string
        self.connection_string = {}

    @classmethod
    def from_crawler(cls, crawler):
        return cls(connection_string=crawler.settings.get('REDIS'))

    def open_spider(self, spider):

        self.client = Redis(**self.connection_string)

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        storage_name = f'{spider.name}:feed'
        self.client.lpush(storage_name, json.dumps(spider.produce_feed(item)))

        return item
