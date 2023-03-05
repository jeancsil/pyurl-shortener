from src.database_loader import Database


class DuplicationChecker:
    """
    Checks for duplicated URLs in the local database.
    """
    db = None

    def __init__(self, database: Database):
        """
        The format of this hashset is:
        _hashset[code] = URL
        {
            "code": "https://url.com/,
            "xyz": "https://xyz-website.com/
        }
        """
        self.db = database

    def url_exists(self, url: str) -> bool:
        """Returns whether the full URL already exists in the values of the hashset"""
        return self.db.contains_url(url)

    def short_code_exists(self, code: str) -> bool:
        """Returns whether the code already exists in the key of the hashset"""
        return self.db.contains_code(code)
