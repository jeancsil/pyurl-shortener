import pytest

from src.invalid_url_error import InvalidURLError
from src.url_validator import UrlValidator


class TestUrlShortener:
    """Test for the URL validator"""

    def test_invalid_url_returns_none(self):
        with pytest.raises(InvalidURLError):
            UrlValidator.validate("")

    def test_valid_https_url_returns_does_not_raise_error(self):
        try:
            UrlValidator.validate("https://www.google.com.br/path-number-1/?param1=value1&q=query")
        except InvalidURLError:
            pytest.fail("Valid URL raised an exception.")

    def test_valid_http_url_returns_does_not_raise_error(self):
        try:
            UrlValidator.validate("http://www.google.com.br/path-number-1/?param1=value1&q=query")
        except InvalidURLError:
            pytest.fail("Valid URL raised an exception.")

    def test_valid_url_without_protocol_does_not_raise_error(self):
        try:
            UrlValidator.validate("www.youtube.com")
        except InvalidURLError:
            pytest.fail("Valid URL raised an exception.")

    def test_valid_url_with_protocol_does_not_raise_error(self):
        try:
            UrlValidator.validate("http://www.youtube.com")
        except InvalidURLError:
            pytest.fail("Valid URL raised an exception.")

    def test_very_long_url_does_not_raise_error(self):
        try:
            very_long_url = "https://gotos.in/you+have+to+write+a+really+really+long+url+to+get+to+650+characters." \
                            "+like+seriously+you+have+no+idea+how+long+it+has+to+be+650+characters+is+absolutely+" \
                            "freaking+enormous.+You+can+fit+sooooooooooooooooooooooooooooooooo+much+data+into+650+" \
                            "characters.+My+hands+are+getting+tired+typing+this+many+characters.+I+didnt+even+realise" \
                            "+how+long+it+was+going+to+take+to+type+them+all.+So+many+characters.+I'm+bored+now+so+" \
                            "I'll+just+copy+and+paste.+I'm+bored+now+so+I'll+just+copy+and+paste+Vsli+.I'm+bored+now+" \
                            "so+I'll+just+copy+and+paste.I'm+bored+now+so+I'll+just+copy+and+paste.I'm+bored+now+so+" \
                            "I'll+just+copy+and+paste.+It+has+to+be+freaking+enormously+freaking+enormous"

            UrlValidator.validate(very_long_url)
        except InvalidURLError:
            pytest.fail("Valid URL raised an exception.")
