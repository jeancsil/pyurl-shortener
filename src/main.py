import sys

from src.tiny_container import TinyContainer
from src.url_exists_error import URLExistsError
from src.url_shortener import UrlShortener


def main():
    """Loads the 'database' and enables shortening of URLs"""
    if len(sys.argv) < 2:
        print(usage())
        sys.exit()

    container = TinyContainer()
    for url in sys.argv[1:]:
        try:
            container.get_url_validator().validate(url)
            full_url, short_url, code = reduce(container.get_url_shortener(), url)
            add_url_to_database(full_url, short_url, code)
        except URLExistsError:
            print("URL: " + url + " already exists")


def load_database() -> dict:
    database = {}
    with open("./etc/db.tsv", "r", encoding="utf-8") as file:
        for line in file:
            split = line.split('\t')
            key = split[0]
            url = split[1].replace("\n", "")
            database[key] = url
        return database


def add_url_to_database(full_url: str, short_url: str, code: str) -> None:
    with open("./etc/db.tsv", "a", encoding="utf-8") as file:
        file.write(f"{code}\t{full_url}\n")


def reduce(url_shortener: UrlShortener, long_url: str) -> (str, str):
    """Reduces the URL to a shorter one
    :return: full URL, short URL
    """
    code, short_url = url_shortener.reduce(long_url)
    # print(f"{short_url} -> {long_url}")
    return long_url, short_url, code


def usage() -> str:
    """Show script usage"""
    return "Usage:\n  pyurl-shortener http://www.site1.com [https://site2.es]"


if __name__ == '__main__':
    main()
