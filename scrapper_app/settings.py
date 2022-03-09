from uuid import uuid4
import os

BOT_NAME = 'scrapper_app'

SPIDER_MODULES = ['scrapper_app.spiders']
NEWSPIDER_MODULE = 'scrapper_app.spiders'
ROBOTSTXT_OBEY = False

ITEM_PIPELINES = {
    'scrapper_app.pipelines.FeedPipeline': 250,
    'scrapy_redis.pipelines.RedisPipeline': 300,
    'scrapper_app.pipelines.DbPipeline': 500,
}

DATABASE = {
    'drivername': 'postgresql',
    'host': 'localhost',
    'port': '5432',
    'username': 'postgres',
    'password': os.environ.get('PG_PWD'),
    'database': 'movies'
}

SPIDER_MIDDLEWARES = {
    'scrapy_redis.pipelines.RedisPipeline': 250,
}


SCHEDULER = "scrapy_redis.scheduler.Scheduler"
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"
STATS_CLASS = "scrapy_redis.stats.RedisStatsCollector"
SCHEDULER_QUEUE_CLASS = 'scrapy_redis.queue.FifoQueue'

SCHEDULER_PERSIST = True
HTTPCACHE_ENABLED = False
RANDOM_UA_PER_PROXY = True
COOKIES_ENABLED = False

DEFAULT_REQUEST_HEADERS = {
    'Referer': 'http://www.kinopoisk.ru/',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'ru,en-us;q=0.7,en;q=0.3',
    'Accept-Encoding': 'deflate',
    'Accept-Charset': 'windows-1251,utf-8;q=0.7,*;q=0.7',
    'Keep-Alive': '300',
    'Connection': 'keep-alive',
    'Cookie': f'users_info[check_sh_bool]=none; search_last_date=2010-02-19; search_last_month=2010-02;PHPSESSID={uuid4()}'
}

ROTATING_PROXY_LIST_PATH = 'proxies.txt'
NUMBER_OF_PROXIES_TO_FETCH = 50
