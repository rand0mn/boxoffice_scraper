from scrapy_redis.spiders import RedisSpider
from scrapper_app.items import WeeklyBoxOfficeItem
from scrapper_app.loaders import load_box_office


class KpBoxOfficeSpider(RedisSpider):
    """
    Предоставляет парсер страниц еженедельных кассовых сборов kinopoisk.ru.
    """
    name = 'kp_box_office_spider'

    redis_key = 'kp_weekends_spider:feed'

    movie_link_template = 'https://www.kinopoisk.ru/film/{0}/'

    def parse(self, response, **kwargs):
        box_office_table_xpath = './/table//tr[@id]'

        for box_office_rec in response.xpath(box_office_table_xpath):
            yield load_box_office(WeeklyBoxOfficeItem(), box_office_rec, weekend=response.meta['date_start'])

    def produce_feed(self, item):
        return {
            'url': self.movie_link_template.format(item['movie_ref']),
            'meta': {
                'movie_ref': item['movie_ref']
            },
        }
