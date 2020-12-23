from html.parser import HTMLParser
from urllib.parse import parse_qs
from settings import SETTINGS


TARGET_STRING_PREFIX = "mailto:" + SETTINGS["to"]


class ParseNotOnCampus(HTMLParser):
    """parse the link for 'not on campus today' """
    def __init__(self):
        super().__init__()
        self._target = None

    def handle_starttag(self, tag, attrs):
        if tag == "a" and attrs[0][1].startswith(TARGET_STRING_PREFIX):
            self._target = attrs[0][1]

    def get_result(self):
        if self._target is None:
            raise ValueError("Not Found")
        return self._target


def parse_respond_mail(mail_html: str) -> dict:
    parser = ParseNotOnCampus()
    parser.feed(mail_html)
    response_query = parser.get_result()
    return parse_qs(response_query)
