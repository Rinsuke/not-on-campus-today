from urllib.parse import parse_qs
import ParseNotOnCampus

def parse_respond_mail(mail_html: str) -> dict:
    parser = ParseNotOnCampus.ParseNotOnCampus()
    parser.feed(mail_html)

    return parse_qs(parser.get_result())

if __name__ == '__main__':
    pass