import unicodedata
import re


class TakeLast:
    """
    Returns the last non-null/non-empty value from the values received,
    so it's typically used as an output processor to single-valued fields.
    It doesn't receive any ``__init__`` method arguments, nor does it accept Loader contexts.

    Example:

    >>> proc = TakeLast()
    >>> proc(['', 'one', 'two', 'three'])
    'three'
    """
    def __call__(self, values):
        for value in values[::-1]:
            if value is not None and value != '':
                return value


class DropDots:
    def __call__(self, values):
        return values[:-1] if len(values) > 1 else values


class Normalize:
    """
    Returns the NFKC form for the unicode string without
    spaces at the beginning and at the end of the string.
    """
    def __call__(self, value):
        return unicodedata.normalize('NFKC', value).strip()


class ExtractNumber:
    """
    Returns all numeric chars as integer.
    """
    def __call__(self, value):
        return re.sub(r'[^0-9]', '', value)


class ExtractCyrillic:
    """
    Returns all rus chars.
    """
    def __call__(self, value):
        return re.sub(r'[ЁёА-я| ]', '', value)


class AsNone:
    """
    Returns None for empty string.
    """
    def __init__(self, text_to_drop=''):
        self.text_to_drop = text_to_drop

    def __call__(self, value):
        return None if value == self.text_to_drop else value
