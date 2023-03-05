import unittest
from unittest import TestCase
from pytest import raises
from src.duplication_checker import DuplicationChecker
from src.url_exists_error import URLExistsError
from src.url_shortener import UrlShortener
from src.database_loader import Database, DatabaseRow


class TestUrlShortener(TestCase):
    """Test for the URL shortener"""
    url_shortener = None

    @classmethod
    def setUpClass(cls):
        database = Database()
        database.add(DatabaseRow("gh", "https://github.com/jeancsil"))
        cls.url_shortener = UrlShortener(DuplicationChecker(database))

    def test_new_url_is_shorter_than_original(self):
        url = "https://www.google.com/doodles/celebrating-bubble-tea"

        self.assertFalse(len(self.url_shortener.reduce(url)) > len(url))

    def test_existing_url_would_raise_url_exists_error(self):
        """I don't want duplicated URLs with different short codes"""
        with raises(URLExistsError):
            url = "https://github.com/jeancsil"
            self.url_shortener.reduce(url)

    @unittest.skip(reason="Not yet implemented")
    def test_similar_existing_url_would_raise_url_exists_error(self):
        """I don't want duplicated URLs with different short codes"""
        with raises(URLExistsError):
            url = "https://github.com/jeancsil/"
            self.url_shortener.reduce(url)
