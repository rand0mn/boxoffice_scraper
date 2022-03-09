from scrapy.loader import ItemLoader
from scrapper_app.items import WeeklyBoxOfficeItem, MovieDetailsItem
from copy import deepcopy


def load_weekend(item, selector) -> WeeklyBoxOfficeItem:
    loader = ItemLoader(item, selector)

    loader.add_xpath('date_range', './text()')
    loader.add_xpath('date_start', './@value')

    return loader.load_item()


def load_box_office(item, selector, **kwargs) -> WeeklyBoxOfficeItem:
    loader = ItemLoader(deepcopy(item), selector)

    loader.add_value('weekend', kwargs['weekend'])
    loader.add_xpath('movie_ref', './td[2]//@href')

    loader.add_xpath('distributor', './td[3]/a/text()')
    loader.add_xpath('n_weekends', './td[3]/span/text()'),
    loader.add_xpath('weekend_gross', './td[4]//text()')
    loader.add_xpath('weekend_session_gross', './td[4]//text()')
    loader.add_xpath('gross', './td[5]//text()')
    loader.add_xpath('session_gross', './td[5]//text()')
    loader.add_xpath('weekend_viewers', './td[6]//text()')
    loader.add_xpath('viewers', './td[7]//text()')
    loader.add_xpath('n_copies', './td[8]//text()')

    return loader.load_item()


def load_movie_details(item, selector, id=None) -> MovieDetailsItem:
    loader = ItemLoader(item, selector)

    loader.add_value('id', id)

    loader.add_xpath('name', '//h1[@itemprop="name"]/span/text()')
    loader.add_xpath('origin_name', '//h1[@itemprop="name"]/following-sibling::div/span[1]/text()')
    loader.add_xpath('year', '//div[text()="Год производства"]/following-sibling::node()//a/text()')
    loader.add_xpath('countries', '//div[text()="Страна"]/following-sibling::node()//a/text()')
    loader.add_xpath('genres', '//div[text()="Жанр"]/following-sibling::node()//a[text()!="слова"]/text()')
    loader.add_xpath('certificate', '//div[text()="Возраст"]/following-sibling::node()//text()')
    loader.add_xpath('mpaa', '//div[text()="Рейтинг MPAA"]/following-sibling::node()//text()')
    loader.add_xpath('duration', '//div[text()="Время"]/following-sibling::node()//text()')

    loader.add_xpath('director', '//div[text()="Режиссер"]/following-sibling::node()/a/text()')
    loader.add_xpath('writer', '//div[text()="Сценарий"]/following-sibling::node()/a/text()')
    loader.add_xpath('producer', '//div[text()="Продюсер"]/following-sibling::node()/a/text()')
    loader.add_xpath('operator', '//div[text()="Оператор"]/following-sibling::node()/a/text()')
    loader.add_xpath('composer', '//div[text()="Композитор"]/following-sibling::node()/a/text()')
    loader.add_xpath('design', '//div[text()="Художник"]/following-sibling::node()/a/text()')
    loader.add_xpath('editor', '//div[text()="Монтаж"]/following-sibling::node()/a/text()')
    loader.add_xpath('actor', '(//div[contains(@class, "film-crew-block")]//ul)[1]//a[@itemprop="actor"]/text()')

    loader.add_xpath('user_score', '(//span[contains(@class, "film-rating-value")]/text())[1]')
    loader.add_xpath('critic_score', '(//span[contains(@class, "film-rating-value")]/text())[2]')
    loader.add_xpath('ru_critic_score', '(//span[contains(@class, "film-rating-value")]/text())[3]')

    return loader.load_item()
