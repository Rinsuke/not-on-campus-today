import email
import imaplib
from email.header import decode_header


class ReadMail:
    def __init__(self, username: str, password: str, imap_server: str, port=993):
        self._username = username
        self._password = password
        self._imap = imaplib.IMAP4_SSL(imap_server, port)
        self._login()
        self._content = None

    def _login(self):
        """login to imap mail server"""
        try:
            self._imap.login(self._username, self._password)
        except imaplib.IMAP4.error:
            raise

    def get_mail(self, num_from_top: int):
        """get the nth-index email from inbox, assign self._content to a message object of the email's content"""
        status, total_messages = self._imap.select()
        if status != 'OK':
            raise imaplib.IMAP4.error("Failed to load inbox, check your internet connection")
        # fetch the nth mail
        response, message = self._imap.fetch(str(int(total_messages[0]) - num_from_top), "(RFC822)")
        # response should be "OK", actual email content is message[0][1]
        if response != "OK":
            raise imaplib.IMAP4.error("Failed to fetch email, check your internet connection")
        self._content = email.message_from_bytes(message[0][1])  # convert from byte to message object

    def get_subject(self) -> str:
        """returns the subject of email"""
        if self._content is None:
            raise TypeError("Failed to load email, have you successfully fetched using get_mail method?")
        return decode_header(self._content["Subject"])[0][0]

    def get_sender(self) -> str:
        """returns the sender of email"""
        if self._content is None:
            raise TypeError("Failed to load email, have you successfully fetched using get_mail method?")
        return decode_header(self._content.get("From"))[0][0]

    def get_html(self) -> str:
        """returns the html part of email as string"""
        for p in self._content.walk():
            if p.get_content_type() == "text/html":
                return p.get_payload(decode=True).decode()
