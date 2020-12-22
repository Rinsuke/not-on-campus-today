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
        try:
            self._imap.login(self._username, self._password)
        except Exception as e:
            # login failed
            # TODO: handle exception
            print(e)
            raise

    def get_mail(self, num_from_top: int):
        """get the nth email from inbox, assign self._content to a message object of the email's content"""
        print(self._imap.list())
        status, total_messages = self._imap.select()
        if status != 'OK':
            raise Exception
        # fetch the nth mail
        response, message = self._imap.fetch(str(int(total_messages[0]) - num_from_top + 1), "(RFC822)")
        # response should be "OK", actual email content is message[0][1]
        if response != "OK":
            raise Exception
        self._content = email.message_from_bytes(message[0][1])  # convert from byte to message object

    def get_subject(self):
        if self._content is None:
            raise TypeError
        return decode_header(self._content["Subject"])[0][0]

    def get_sender(self):
        if self._content is None:
            raise TypeError
        return decode_header(self._content.get("From"))[0][0]

    def get_html(self):
        if self._content.is_multipart():
            return [p.get_payload(decode=True).decode()  for p in self._content.walk()  if p.get_content_type() == "text/html"]
        # TODO: handle non-multipart

    def get_plaintext(self):
        if self._content.is_multipart():
            for p in self._content.walk():
                if p.get_content_type() == "text/plain":
                    return p.get_payload(decode=True).decode()



