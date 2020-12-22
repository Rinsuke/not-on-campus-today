from html.parser import HTMLParser
from urllib.parse import parse_qs

TARGET_STRING_PREFIX = "mailto:uci@service-now.com?subject=Re%3A%20Not%20on%20campus%20today"


class ParseNotOnCampus(HTMLParser):
    def __init__(self):
        super().__init__()
        self._target = None

    def handle_starttag(self, tag, attrs):
        if tag == "a" and attrs[0][1].startswith(TARGET_STRING_PREFIX):
            self._target = attrs[0][1]

    def get_result(self):
        if self._target is None:
            return ValueError("Not Found")
        return self._target


def parse_respond_mail(mail_html: str) -> dict:
    parser = ParseNotOnCampus()
    parser.feed(mail_html)

    return parse_qs(parser.get_result())
