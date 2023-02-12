class DuplicationChecker:
    """
    Checks for duplicated URLs in the local database.
    """

    def __init__(self, database: dict):
        """
        The format of this hashset is:
        _hashset[code] = URL
        {
            "code": "https://url.com/,
            "xyz": "https://xyz-website.com/
        }
        """
        self._hashset = database

    def url_exists(self, url: str) -> bool:
        """Returns whether the full URL already exists in the values of the hashset"""
        return url in self._hashset.values()

    def short_code_exists(self, code: str) -> bool:
        """Returns whether the code already exists in the key of the hashset"""
        return code in self._hashset.keys()
