# SCRIPT FOR SENDING EMAILS 
# In order to use a gmail follow these steps:
#   1. Go to google account 
#   2. In the security section allow 2-step verification
#   3. Generate an app password
#   4. Copy that password into the global variable PASSWORD

import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

EMAIL_FROM = "email@gmail.com"
PASSWORD   = "password"
HOST       = "smtp.gmail.com"
PORT       = 587
EMAILS_TO  = {"email1@gmail.com": "ali",
              "email2@gmail.com": "bob"}

content    = Template(Path("content.txt").read_text())

for email_to, name in EMAILS_TO.items():
    print("start")
    email = EmailMessage()
    email['from'] = "Yuma Takahashi"
    email['to']   = email_to
    email['subject'] = "TESTING PYTHON EMAIL SCRIPT"

    email.set_content(content.substitute({"towho": name}))
    with smtplib.SMTP(host=HOST, port=PORT) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.login(EMAIL_FROM, PASSWORD)
        smtp.send_message(email)
    print("end")

print("\033[92mAll done\033[0m")
     