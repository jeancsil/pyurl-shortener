from unittest import TestCase
from pytest import raises
from src.duplication_checker import DuplicationChecker
from src.url_exists_error import URLExistsError
from src.url_shortener import UrlShortener


class TestUrlShortener(TestCase):
    """Test for the URL shortener"""
    url_shortener = None

    @classmethod
    def setUpClass(cls):
        database = {}
        with open("./etc/db.tsv", "r", encoding="utf-8") as file:
            for line in file:
                split = line.split('\t')
                key = split[0]
                url = split[1]
                database[key] = url
        cls.url_shortener = UrlShortener(DuplicationChecker(database))

    def test_new_url_is_shorter_than_original(self):
        url = "https://www.google.com/doodles/celebrating-bubble-tea"

        self.assertFalse(len(self.url_shortener.reduce(url)) > len(url))

    def test_existing_url_would_raise_url_exists_error(self):
        """I don't want duplicated URLs with different short codes"""
        with raises(URLExistsError):
            url = "https://github.com/jeancsil"
            self.url_shortener.reduce(url)
