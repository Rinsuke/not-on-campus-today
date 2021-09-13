SETTINGS = {
  # change these to your email address and password
  "netID": "panteater@uci.edu",
  "password": "ZotZotZot",

  # maximum number of emails checked before failure,
  # if you have tons of email each day you want to increase this number
  "max_number_of_emails": 20,

  # 0: not on campus today
  # 1: no
  # 2: yes
  "response": 1,

  # do not modify these (unless something fails)
  "from": "uci@service-now.com",  # address where daily checkin email come from
  "to": "uci@service-now.com",    # address where you send responses to
  "subject": "UCI Student Daily Symptom Monitoring",  # subject of that email
  "imap": "imap.gmail.com",       # gmail imap server address
  "imap_port": 993,               # gmail imap port
  "smtp": "smtp.gmail.com",       # gmail smtp server address
  "smtp_port": 465,               # gmail smtp port

}
