import smtplib

import mail.send_mail as send
import mail.read_mail as read
import parse.ParseNotOnCampus as parse
from settings import SETTINGS
from imaplib import IMAP4

_DEBUG = False


def read_inbox(mail: read.ReadMail) -> dict:
    """read emails from inbox and find the correct response link, returns the link as a dict with arguments"""
    for i in range(SETTINGS["max_number_of_emails"]):
        mail.get_mail(i)
        if _DEBUG:
            print(f"Checking mail at index {i}:")
            print(f"    Subject: {mail.get_subject()}")
            print(f"    From: {mail.get_sender()}")
        if mail.get_subject() == SETTINGS["subject"] and (SETTINGS["from"] in mail.get_sender()):
            # found the correct email, parse html text and find response link
            try:
                response = parse.parse_respond_mail(mail.get_html())
            except ValueError:  # link not found, keep searching
                continue
            else:  # found link
                return response
    raise ValueError("Matching daily symptom check email not found, consider increase the number of emails checked and "
                     + "make sure email is delivered to your inbox (not spam folder)")


def send_mail(mail: send.SendMail, response: dict):
    """send out response email"""
    mail.set(  # construct parts of email to send
        subject=response["mailto:" + SETTINGS["to"] + "?subject"][0],
        sender=SETTINGS["netID"],
        recipient=SETTINGS["to"],
        content=response["body"][0]
    )
    mail.send()
    mail.quit()


def main():
    try:
        response = read_inbox(
            read.ReadMail(SETTINGS["netID"], SETTINGS["password"], SETTINGS["imap"], SETTINGS["imap_port"])
        )
    except ValueError as e:  # not found
        print(str(e.args))
        exit(1)
    except IMAP4.error as e:  # network error
        print("="*20)
        print("FAILED: failed to fetch email from email")
        print(str(e))
        exit(1)

    try:
        send_mail(
            send.SendMail(SETTINGS["netID"], SETTINGS["password"], SETTINGS["smtp"], SETTINGS["smtp_port"]),
            response
        )
    except smtplib.SMTPException as e:
        print("="*20)
        print("FAILED: No email was sent")
        print(f"{e}: {e.args}")
        exit(1)
    else:
        print("=" * 20)
        print(f"SUCCESS: email sent to {SETTINGS['to']}")
        exit()


if __name__ == '__main__':
    main()
