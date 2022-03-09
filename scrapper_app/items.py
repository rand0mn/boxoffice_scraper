from scrapy.item import Item, Field
from itemloaders.processors import TakeFirst, MapCompose, Compose, Join
from scrapper_app.processors import Normalize, ExtractNumber, TakeLast, AsNone


class WeeklyBoxOfficeItem(Item):
    """Scrapped data for movie's weekly box office."""

    movie_ref = Field(
        input_processor=MapCompose(Normalize(), ExtractNumber()),
        output_processor=Compose(TakeFirst()),
    )
    weekend = Field(
        output_processor=Compose(TakeFirst()),
    )
    distributor = Field(
        input_processor=MapCompose(Normalize()),
        output_processor=Compose(TakeFirst()),
    )
    n_weekends = Field(
        input_processor=MapCompose(Normalize(), ExtractNumber()),
        output_processor=Compose(TakeFirst()),
    )
    weekend_gross = Field(
        input_processor=MapCompose(Normalize(), ExtractNumber()),
        output_processor=Compose(TakeFirst()),
    )
    weekend_session_gross = Field(
        input_processor=MapCompose(Normalize(), ExtractNumber()),
        output_processor=Compose(TakeLast()),
    )
    gross = Field(
        input_processor=MapCompose(Normalize(), ExtractNumber()),
        output_processor=Compose(TakeFirst()),
    )
    session_gross = Field(
        input_processor=MapCompose(Normalize(), ExtractNumber()),
        output_processor=Compose(TakeLast()),
    )
    weekend_viewers = Field(
        input_processor=MapCompose(Normalize(), ExtractNumber()),
        output_processor=Compose(TakeFirst()),
    )
    viewers = Field(
        input_processor=MapCompose(Normalize(), ExtractNumber()),
        output_processor=Compose(TakeFirst()),
    )
    n_copies = Field(
        input_processor=MapCompose(Normalize(), ExtractNumber()),
        output_processor=Compose(TakeFirst()),
    )


class WeekendItem(Item):
    date_range = Field(
        input_processor=MapCompose(Normalize()),
        output_processor=Compose(TakeFirst()),
    )
    date_start = Field(
        input_processor=MapCompose(Normalize()),
        output_processor=Compose(TakeFirst()),
    )


class MovieDetailsItem(Item):
    id = Field(
        output_processor=Compose(TakeFirst()),
    )
    name = Field(
        input_processor=MapCompose(Normalize()),
        output_processor=Compose(TakeFirst()),
    )
    origin_name = Field(
        input_processor=MapCompose(Normalize()),
        output_processor=Compose(TakeFirst()),
    )
    year = Field(
        input_processor=MapCompose(Normalize(), ExtractNumber()),
        output_processor=Compose(TakeFirst()),
    )
    countries = Field(
        input_processor=MapCompose(Normalize()),
        output_processor=Compose(Join(',')),
    )
    genres = Field(
        input_processor=MapCompose(Normalize()),
        output_processor=Compose(Join(',')),
    )
    certificate = Field(
        input_processor=MapCompose(Normalize()),
        output_processor=Compose(TakeFirst()),
    )
    mpaa = Field(
        input_processor=MapCompose(Normalize()),
        output_processor=Compose(TakeFirst()),
    )
    duration = Field(
        input_processor=MapCompose(lambda s: s.split('/'), Normalize()),
        output_processor=Compose(TakeLast()),
    )
    director = Field(
        input_processor=MapCompose(Normalize(), AsNone('...')),
        output_processor=Compose(Join(',')),
    )
    writer = Field(
        input_processor=MapCompose(Normalize(), AsNone('...')),
        output_processor=Compose(Join(',')),
    )
    producer = Field(
        input_processor=MapCompose(Normalize(), AsNone('...')),
        output_processor=Compose(Join(',')),
    )
    operator = Field(
        input_processor=MapCompose(Normalize(), AsNone('...')),
        output_processor=Compose(Join(',')),
    )
    composer = Field(
        input_processor=MapCompose(Normalize(), AsNone('...')),
        output_processor=Compose(Join(',')),
    )
    design = Field(
        input_processor=MapCompose(Normalize(), AsNone('...')),
        output_processor=Compose(Join(',')),
    )
    editor = Field(
        input_processor=MapCompose(Normalize(), AsNone('...')),
        output_processor=Compose(Join(',')),
    )
    actor = Field(
        input_processor=MapCompose(Normalize(), AsNone('...')),
        output_processor=Compose(Join(',')),
    )
    user_score = Field(
        input_processor=MapCompose(Normalize()),
        output_processor=Compose(TakeFirst()),
    )
    critic_score = Field(
        input_processor=MapCompose(Normalize()),
        output_processor=Compose(TakeFirst()),
    )
    ru_critic_score = Field(
        input_processor=MapCompose(Normalize()),
        output_processor=Compose(TakeFirst()),
    )
