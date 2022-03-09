from scrapper_app.db.db import DB
from scrapper_app.models import Movie, Weekend, WeeklyBoxOffice
from sqlalchemy.exc import SQLAlchemyError, IntegrityError


class DbPipeline:
    """
    Предоставляет pipeline для сохранения item в postgres.
    """

    def __init__(self, connection_string):
        self.connection_string = connection_string

    @classmethod
    def from_crawler(cls, crawler):
        return cls(connection_string=crawler.settings.get('DATABASE'))

    def open_spider(self, spider):
        self.session = DB(self.connection_string).create_session()

    def close_spider(self, spider):
        self.session.close()

    def process_item(self, item, spider):
        try:
            if spider.name == 'kp_movies_spider':
                movie = Movie(**item)
                self.session.add(movie)
            elif spider.name == 'kp_weekends_spider':
                weekend = Weekend(**item)
                self.session.add(weekend)
            elif spider.name == 'kp_box_office_spider':
                box_office = WeeklyBoxOffice(**item)
                self.session.add(box_office)

            self.session.commit()
        except SQLAlchemyError or IntegrityError:
            self.session.rollback()

        return item
