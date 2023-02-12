from simple_http_server import Redirect
from simple_http_server import route, controller, HttpError, Response
from simple_http_server import server

# TODO
# Load the tsv file with the saved URL's into the hashset
HTML = """
<html>
    <head>
    <meta charset="UTF-8">
    <style type="text/css">
        body {
            font-size: 14px;
            font-family: arial,sans-serif;
            color: #bdc1c6;
        }
        body {
            background: #202124;
        }
        a {
          color: #bdc1c6;
          text-decoration: none;
        }
    </style>
    </head>
    <body>{}</body>
</html>
"""


@controller
class HttpServerController:
    """HTTP Server that redirects the short URLs to the full URLs"""

    def __init__(self) -> None:
        self._hashset = dict()
        print("Loading the dict.........")

        with open("./etc/db.tsv") as file:
            for line in file:
                split = line.split('\t')
                key = split[0]
                url = split[1]
                print("Key: " + key)
                print("URL: " + url)
                self._hashset[key] = url
        # print(self._hashset)

    @route("/", method="GET", params="u")
    def root(self, code: str):
        if code not in self._hashset:
            print("Url is None for the code: {}".format(code))
            raise HttpError(404, "Not found")

        url = self._hashset[code]

        print("Redirecting to {}".format(url))
        return Redirect(url=url)

    @route("/list", method="GET")
    def list_routes(self):
        body = ""
        for key in self._hashset:
            body += '<a href="{}">{}({})</a><br/>'.format(self._hashset[key], self._hashset[key], key)

        return Response(body=HTML.replace("{}", body), status_code=200)

    @route("/favicon.ico", method="GET")
    def favicon(self):
        return Response(status_code=204)


server.start(port=8081, prefer_coroutine=True)
