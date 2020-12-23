# not-on-campus-today

> Hi Anteater,

> As part of UCI’s Living Well campaign, we want to remind you to take care of your own health and that of others.

> [Not on campus today](https://uci.edu/coronavirus/)

> No further action is required.

> Your answer is confidential.

This script searches your inbox for this email and respond **Not on campus today** for you.

## Usage:
### Requirements:
 - Python 3.7+
 
### Run:
1. Clone this repo or download as .zip
 
 ```
 git clone https://github.com/Rinsuke/not-on-campus-today.git
 cd ./not-on-campus-today/
 ```

2. Make sure [IMAP](https://support.google.com/mail/answer/7126229) 
and [allow less secure app access](https://myaccount.google.com/lesssecureapps) are turned on

3. Open `settings.py` with your favorite text editor 
~~```vi ./settings.py```~~

4. Replace the first few lines with your email address and password

5. Run main.py

```
python3 ./main.py
```

6. (optional) Schedule this script to run automatically every day at 3am (Guide for [Windows](https://www.windowscentral.com/how-create-automated-task-using-task-scheduler-windows-10)
[Linux](https://www.howtogeek.com/101288/how-to-schedule-tasks-on-linux-an-introduction-to-crontab-files/) )


## Warning:
Your password is stored **IN PLAIN TEXT**, anyone ***with access to your computer*** can see it. **Use this script at your own risk!**

#### Always Practice Good Password Habit:
- Change your password periodically
- Do not use the same password on multiple sites
