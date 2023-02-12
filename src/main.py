import sys

from duplication_checker import DuplicationChecker
from url_shortener import UrlShortener


def main():
    """Loads the 'database' and enables shortening of URLs"""
    if len(sys.argv) < 2:
        print(usage())
        sys.exit()

    database = {}
    with open("./etc/db.tsv", "r", encoding="utf-8") as file:
        for line in file:
            split = line.split('\t')
            key = split[0]
            url = split[1]
            database[key] = url

    url_shortener = UrlShortener(DuplicationChecker(database))

    for param in sys.argv[1:]:
        reduce(url_shortener, param)


def reduce(url_shortener: UrlShortener, full_url: str):
    """Reduces the URL to a shorter one"""
    print(full_url)
    print(url_shortener.reduce(full_url))


def usage() -> str:
    """Show script usage"""
    return "Usage:\n  pyurl-shortener http://www.site1.com [https://site2.es]"


if __name__ == '__main__':
    main()
