import io
from unittest import TestCase

from src.duplication_checker import DuplicationChecker


class TestDuplicationChecker(TestCase):
    @classmethod
    def setUpClass(cls):
        database_stub = dict({"g": "https://www.google.com/"})
        cls.duplication_checker = DuplicationChecker(database_stub)

    def test_finds_duplicated_code_in_database(self):
        self.assertFalse(self.duplication_checker.valid("g"))

    def test_does_not_find_duplicated_code_in_database(self):
        self.assertTrue(self.duplication_checker.valid("uniq"))
