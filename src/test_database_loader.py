from unittest import TestCase

from src.database_loader import DatabaseLoader, Database, DatabaseRow


class TestDatabaseLoader(TestCase):
    """Test for DatabaseLoader class"""

    def setUp(self) -> None:
        input_dict = ["g	https://www.google.com/\n",
                      "gh	https://github.com/jeancsil"]
        self.database = DatabaseLoader().load_from_dict(input_dict)

    def test_correct_instance(self):
        self.assertIsInstance(self.database, Database)

    def test_db_contains_2_rows(self):
        self.assertEqual(len(self.database.get()), 2)

    def test_db_contains_specific_row(self):
        self.assertTrue(DatabaseRow("gh", "https://github.com/jeancsil") in self.database.get())

    def test_db_does_not_contain_specific_row(self):
        self.assertFalse(DatabaseRow("gh", "http://github.com/jeancsil") in self.database.get())
