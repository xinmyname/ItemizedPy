"""Marks a class as a singleton"""
class Singleton(type):
    """Marks a class as a singleton"""

    _instances = {}

    def __call__(cls, *args, **kwargs):

        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)

        return cls._instances[cls]
