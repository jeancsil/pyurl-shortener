from src.database_loader import Database
from src.database_loader import DatabaseLoader
from src.duplication_checker import DuplicationChecker
from src.url_shortener import UrlShortener
from src.url_validator import UrlValidator


class TinyContainer:
    """Tiny DI container not to have a mess in the main.py"""

    def __init__(self):
        database_loader = DatabaseLoader()
        database = database_loader.load()
        duplication_checker = DuplicationChecker(database)
        self.instances = {"database_loader": database_loader,
                          "database": database,
                          "duplication_checker": duplication_checker,
                          "url_shortener": UrlShortener(duplication_checker),
                          "url_validator": UrlValidator()}

    def get_duplication_checker(self) -> DuplicationChecker:
        return self.instances["duplication_checker"]

    def get_url_shortener(self) -> UrlShortener:
        return self.instances["url_shortener"]

    def get_url_validator(self) -> UrlValidator:
        return self.instances["url_validator"]

    def get_database_loader(self) -> DatabaseLoader:
        return self.instances["database_loader"]

    def get_database(self) -> Database:
        return self.instances["database"]
