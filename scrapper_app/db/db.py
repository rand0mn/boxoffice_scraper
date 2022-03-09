from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine.url import URL


class DB:
    """
    Предоставляет сессию БД.
    """
    def __init__(self, connection_string):
        self.engine = create_engine(URL(**connection_string), pool_pre_ping=True)
        self.session = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)

    def create_session(self):
        return self.session()
