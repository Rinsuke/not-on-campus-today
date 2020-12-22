from settings import *
import mail.send_mail as send
import mail.read_mail as read
import parse.ParseNotOnCampus as parse


def main():
    read_mail = read.ReadMail(SETTINGS["netID"], SETTINGS["password"], SETTINGS["imap"], SETTINGS["imap_port"])

    mail_content = None
    for i in range(SETTINGS["max_number_of_emails"]):
        read_mail.get_mail(i)
        print(read_mail.get_subject())
        print(read_mail.get_sender())
        if read_mail.get_subject() == SETTINGS["subject"] and (SETTINGS["from"] in read_mail.get_sender()):
            # found the correct email
            mail_content = read_mail.get_html()
            break

    if mail_content is None:
        # TODO: raise correct exception
        raise Exception

    # mail_content is email text in html format
    # parse html and find the correct link
    response = parse.parse_respond_mail(mail_content)

    send_mail = send.SendMail(SETTINGS["netID"], SETTINGS["password"], SETTINGS["smtp"], SETTINGS["smtp_port"])
    send_mail.set(
        subject=response["mailto:"+"uci@service-now.com"+"?subject"][0],
        sender=SETTINGS["netID"],
        recipient=SETTINGS["to"],
        content=response["body"][0]
    )
    send_mail.send()
    send_mail.quit()


if __name__ == '__main__':
    main()
