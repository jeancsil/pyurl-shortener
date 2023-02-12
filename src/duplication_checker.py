class DuplicationChecker:
    """
    Checks for duplicated URLs in the local database.
    """

    def __init__(self, database: dict):
        """
        The format of this hashset is:
        _hashset[code] = URL
        """
        self._hashset = database

    def exists(self, url: str) -> bool:
        """Returns whether the code already exists in the hashset"""
        return url in self._hashset.values()
