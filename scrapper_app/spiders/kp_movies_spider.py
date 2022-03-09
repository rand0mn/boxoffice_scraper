from scrapy_redis.spiders import RedisSpider
from scrapper_app.items import MovieDetailsItem
from scrapper_app.loaders import load_movie_details
import os


class KpMoviesSpider(RedisSpider):
    """
    Предоставляет парсер страниц кинофильмов с kinopoisk.ru.
    """

    name = 'kp_movies_spider'
    redis_key = 'movies_2021'

    custom_settings = {
        'ITEM_PIPELINES': {
            'scrapy_redis.pipelines.RedisPipeline': 300,
            'scrapper_app.pipelines.DbPipeline': 500,
        },
        'DOWNLOADER_MIDDLEWARES': {
            'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
            # Бесплатные прокси, как альтернатива scrapy_zyte_smartproxy
            # 'rotating_free_proxies.middlewares.RotatingProxyMiddleware': 610,
            # 'scrapper_app.ban_policy.CaptchaPolicy': 620,
            'scrapy_zyte_smartproxy.ZyteSmartProxyMiddleware': 610,
            'scrapy_user_agents.middlewares.RandomUserAgentMiddleware': 800,
        },
        'AUTOTHROTTLE_ENABLED': True,
        'AUTOTHROTTLE_START_DELAY': 60*5,
        'DOWNLOAD_DELAY': 60*5,
        'DOWNLOAD_TIMEOUT': 600,
        'CONCURRENT_REQUESTS': 64,
        'CONCURRENT_REQUESTS_PER_DOMAIN': 64,
    }

    zyte_smartproxy_enabled = True
    zyte_smartproxy_apikey = os.environ.get('ZYTE_API_KEY')

    def parse(self, response, **kwargs):
        yield load_movie_details(MovieDetailsItem(), response, id=response.meta['movie_ref'])
