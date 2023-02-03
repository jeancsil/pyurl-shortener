class DuplicationChecker:
    def __init__(self, database: dict):
        """
        The format of this hashset is:
        _hashset[code] = URL
        """
        self._hashset = database

    def valid(self, code: str) -> bool:
        return code not in self._hashset
