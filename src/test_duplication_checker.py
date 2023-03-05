from unittest import TestCase

from src.database_loader import DatabaseLoader
from src.duplication_checker import DuplicationChecker


class TestDuplicationChecker(TestCase):
    """Test for Duplication Checker class"""

    @classmethod
    def setUpClass(cls):
        database_stub = ["g\thttps://www.google.com/",
                         "gh\thttps://github.com/jeancsil",
                         "ZJCzE\thttps://gotos.in/you+have+to+write+a+really+really+long+url+to+get+to+650+characters",
                         "uniqode\thttps://gotos.in/long+url+with+a+break+line+at+the+end\n"]
        cls.duplication_checker = DuplicationChecker(DatabaseLoader().load_from_dict(database_stub))

    def test_finds_duplicated_code_in_database(self):
        self.assertTrue(self.duplication_checker.short_code_exists("g"))
        self.assertTrue(self.duplication_checker.short_code_exists("ZJCzE"))

    def test_lowercase_version_of_code_is_not_the_same(self):
        self.assertFalse(self.duplication_checker.short_code_exists("zjcze"))

    def test_does_not_find_duplicated_code_in_database(self):
        self.assertFalse(self.duplication_checker.short_code_exists("uniq"))

    def test_finds_duplicated_url_in_database(self):
        self.assertTrue(self.duplication_checker.url_exists("https://www.google.com/"))

    def test_does_not_find_similar_url_in_database(self):
        self.assertFalse(self.duplication_checker.url_exists("https://www.google.es"))

    def test_finds_long_url_in_database(self):
        self.assertTrue(self.duplication_checker.url_exists(
            "https://gotos.in/you+have+to+write+a+really+really+long+url+to+get+to+650+characters"))

    def test_finds_url_without_break_line(self):
        self.assertTrue(self.duplication_checker.url_exists("https://gotos.in/long+url+with+a+break+line+at+the+end"))
