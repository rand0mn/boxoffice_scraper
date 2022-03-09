from scrapper_app.db.db import DB
from sqlalchemy import text
from redis import Redis
import os
import json

connection_string = {
    'drivername': 'postgresql',
    'host': 'localhost',
    'port': '5432',
    'username': 'postgres',
    'password': os.environ.get('PG_PSWD'),
    'database': 'movies'
}

db = DB(connection_string=connection_string).engine

q = text('''
    select distinct bo.movie_ref
        from weekly_box_offices bo
        where bo.movie_ref not in (select id from movies)
    ''')


def convert(kp_id):
    return json.dumps({
        "url": f"https://www.kinopoisk.ru/film/{str(kp_id)}/",
        "meta": {
            "movie_ref": f"{str(kp_id)}"
        }
    })


res = db.execute(q)
movie_links = [convert(x[0]) for x in db.execute(q)]

redis = Redis()

redis.lpush('movies_2021', *movie_links)

