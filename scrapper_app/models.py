from sqlalchemy import Column, String, Date, Integer, BigInteger, SmallInteger
from scrapper_app.db.model_base import ModelBase


class Movie(ModelBase):
    __tablename__ = 'movies'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    origin_name = Column(String, nullable=True)
    year = Column(SmallInteger, nullable=False)
    countries = Column(String)
    genres = Column(String)
    certificate = Column(String)
    mpaa = Column(String)
    duration = Column(String)
    director = Column(String)
    writer = Column(String)
    producer = Column(String)
    operator = Column(String)
    composer = Column(String)
    design = Column(String)
    editor = Column(String)
    actor = Column(String)
    user_score = Column(String)
    critic_score = Column(String)
    ru_critic_score = Column(String)


class Weekend(ModelBase):
    __tablename__ = 'weekends'

    id = Column(Integer, primary_key=True)
    date_range = Column(String(length=30), nullable=False)
    date_start = Column(Date, nullable=False, unique=True)


class WeeklyBoxOffice(ModelBase):
    __tablename__ = 'weekly_box_offices'

    id = Column(Integer, primary_key=True)
    weekend_gross = Column(Integer)
    weekend_session_gross = Column(Integer)
    gross = Column(BigInteger)
    session_gross = Column(Integer)
    weekend_viewers = Column(Integer)
    viewers = Column(BigInteger)
    n_copies = Column(SmallInteger)
    n_weekends = Column(SmallInteger)
    distributor = Column(String)

    movie_ref = Column(Integer, nullable=False)
    weekend = Column(String, nullable=False)
