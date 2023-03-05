from dataclasses import dataclass


@dataclass
class DatabaseRow:
    """Dataclass for the database row"""
    key: str
    url: str

    def __hash__(self):
        return hash((self.key, self.url))


class Database:
    """Dataclass for the database"""

    def __init__(self):
        self.database_rows = set()

    def add(self, row: DatabaseRow):
        self.database_rows.add(row)

    def get(self):
        return self.database_rows

    def contains_url(self, url):
        for row in self.database_rows:
            if url == row.url:
                return True
        return False

    def contains_code(self, code):
        for row in self.database_rows:
            if code == row.key:
                return True
        return False


class DatabaseLoader:
    """Loads the database into an internally known format"""

    def __init__(self):
        self.database = Database()

    def load_from_dict(self, input_dict) -> Database:
        self.__read_lines_and_get_database(input_dict)
        return self.database

    def load(self, path=None) -> Database:
        load_from = "./etc/db.tsv"
        if path:
            load_from = path

        with open(load_from, "r", encoding="utf-8") as file:
            self.__read_lines_and_get_database(file)
            return self.database

    def __read_lines_and_get_database(self, lines) -> None:
        for line in lines:
            split = line.split('\t')
            key = split[0]
            url = split[1].replace("\n", "")
            self.database.add(row=DatabaseRow(key, url))
