from sqlalchemy.ext.declarative import as_declarative, declared_attr
import json


@as_declarative()
class ModelBase:
    """
    Предоставляет базовый класс MAP
    """
    __name__: str

    @classmethod
    def from_dict(cls, **kwargs):
        """
        Создает сущность на основе словаря, при условии наличия поля в сущности.
        :param kwargs:
        :return: ModelBase
        """
        obj = cls()
        for key, value in cls.filter_kw_params(**kwargs).items():
            setattr(obj, key, value)
        return obj

    @classmethod
    def filter_kw_params(cls, **kwargs):
        """
        Фильтрует словарь на основе полей сущности.
        :param kwargs:
        :return: ModelBase
        """
        class_attr = cls.__dict__.keys()
        return {key: value for key, value in kwargs.items() if key in class_attr}

    @classmethod
    def get_or_create(cls, session, **kwargs):
        """Получает сущность из кэша или БД, в ином случае создает новую."""
        cache = getattr(session, '_unique_cache', None)
        if cache is None:
            session._unique_cache = cache = {}

        key = (cls, hash(json.dumps(kwargs, sort_keys=True)))
        if key in cache:
            return cache[key]

        params = cls.filter_kw_params(**kwargs)
        with session.no_autoflush:
            q = session.query(cls)
            for key, value in params.items():
                q = q.filter(getattr(cls, key) == value)
            obj = q.first()
            if not obj:
                obj = cls.from_dict(**params)
                session.add(obj)
            cache[key] = obj
            return obj

    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()
