from urllib.parse import urlparse

from src.invalid_url_error import InvalidURLError


class UrlValidator:
    """Validates URL's very basically."""

    @staticmethod
    def validate(url: str) -> None:
        if not url.startswith("http"):
            url = "http://" + url

        result = urlparse(url)

        if not all([result.scheme, result.netloc]):
            raise InvalidURLError()
