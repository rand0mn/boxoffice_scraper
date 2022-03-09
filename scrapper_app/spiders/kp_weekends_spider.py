from datetime import date
from scrapy import Spider, Request

from scrapper_app.items import WeekendItem
from scrapper_app.loaders import load_weekend
from time import sleep


class KpWeekendsSpider(Spider):
    """
    Предоставляет парсер уик-эндов с kinopoisk.ru.
    """

    name = 'kp_weekends_spider'

    def start_requests(self):
        year_link_template = 'https://www.kinopoisk.ru/index.php?level=42&type=rus&year={0}'

        years = range(2007, date.today().year + 1)
        return (Request(year_link_template.format(year), callback=self.parse) for year in years)

    def parse(self, response, **kwargs):
        weekend_dropout_list_xpath = './/select[@name="weekend"]//option'
        if response.status == 302:
            sleep(120)

        for weekend_rec in response.xpath(weekend_dropout_list_xpath):
            yield load_weekend(WeekendItem(), weekend_rec)

    def produce_feed(self, item):
        box_office_link_template = 'https://www.kinopoisk.ru/box/weekend/{0}/type/rus/cur/RUB/view/all/'

        return {
            'url': box_office_link_template.format(item['date_start']),
            'meta': {
                'date_start': item['date_start'],
            }
        }
