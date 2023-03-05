import random
import string

from typing import Tuple

from src.duplication_checker import DuplicationChecker
from src.url_exists_error import URLExistsError


class UrlShortener(DuplicationChecker):
    """Generates a shorter version of the URL"""
    def __init__(self, duplication_checker: DuplicationChecker):
        self.duplication_checker = duplication_checker
        self.base_url = "http://localhost:8081"
        self.alphabet = list(string.ascii_lowercase) + list(string.ascii_uppercase)

    def reduce(self, url: str) -> Tuple[str, str]:
        """
        The number of total combinations possible is calculated as:

        n!/(r!(n-r)!)
        n is the total number of letters
        r is the number of letters you want to choose

        52 letters and I can choose 1: 52!/(1!(52-1)!) = 52
        52 letters and I can choose 2: 52!/(2!(52-2)!) = 1326
        52 letters and I can choose 3: 52!/(3!(52-3)!) = 22100
        52 letters and I can choose 4: 52!/(4!(52-4)!) = 270725
        52 letters and I can choose 5: 52!/(5!(52-5)!) = 2598960
        """
        if self.duplication_checker.url_exists(url):
            raise URLExistsError()

        code = self._get_random_chars(5)
        return code, f"{self.base_url}?u={code}"

    def _get_random_chars(self, length=3):
        code = "".join(random.sample(self.alphabet, k=length))
        while self.duplication_checker.short_code_exists(code):
            code = self._get_random_chars()

        return "".join(random.sample(self.alphabet, k=length))
