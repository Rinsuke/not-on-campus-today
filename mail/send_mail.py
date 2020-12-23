import smtplib
from email.message import EmailMessage


class SendMail:
    def __init__(self, username: str, password: str, smtp_server: str, port=465):
        self._username = username
        self._password = password
        self._smtp = smtplib.SMTP_SSL(smtp_server, port)
        self._login()
        self._message = EmailMessage()

    def _login(self):
        """login to smtp server"""
        try:
            self._smtp.login(self._username, self._password)
        except Exception:
            raise smtplib.SMTPAuthenticationError(
                "Login to SMTP server failed, check your email address and/or password"
            )

    def set_subject(self, subject):
        self._message["Subject"] = subject

    def set_recipient(self, address):
        self._message["To"] = address

    def set_sender(self, address):
        self._message["From"] = address

    def set_content(self, content):
        self._message.set_content(content)

    def set(self, subject, sender, recipient, content):
        self.set_subject(subject)
        self.set_sender(sender)
        self.set_recipient(recipient)
        self.set_content(content)

    def send(self):
        self._smtp.send_message(self._message)

    def quit(self):
        self._smtp.quit()
