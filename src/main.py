import sys

from src.database_loader import DatabaseRow
from src.tiny_container import TinyContainer
from src.url_exists_error import URLExistsError


def main():
    """Loads the 'database' and enables shortening of URLs"""
    if len(sys.argv) < 2:
        print(usage())
        sys.exit()

    container = TinyContainer()
    for url in sys.argv[1:]:
        try:
            container.get_url_validator().validate(url)
            code, _ = container.get_url_shortener().reduce(url)
            container.get_database_loader().add_row(DatabaseRow(code, url))
        except URLExistsError:
            print("URL: " + url + " already exists")


def usage() -> str:
    """Show script usage"""
    return "Usage:\n  pyurl-shortener http://www.site1.com [https://site2.es]"


if __name__ == '__main__':
    main()
