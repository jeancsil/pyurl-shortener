from src.database_loader import DatabaseLoader
from src.duplication_checker import DuplicationChecker
from src.url_shortener import UrlShortener
from src.url_validator import UrlValidator


class TinyContainer:
    """Tiny DI container not to have a mess in the main.py"""

    def __init__(self):
        self.instances = {}
        database = DatabaseLoader().load()
        duplication_checker = DuplicationChecker(database)
        self.instances = {"duplication_checker": duplication_checker,
                          "url_shortener": UrlShortener(duplication_checker),
                          "url_validator": UrlValidator()}

    def get_duplication_checker(self):
        return self.instances["duplication_checker"]

    def get_url_shortener(self):
        return self.instances["url_shortener"]

    def get_url_validator(self):
        return self.instances["url_validator"]
