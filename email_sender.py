import os
import smtplib

friend_name = 'Борис'
my_name = 'Васильев'
email_from = 'from_mail@gmail.com'
email_to = 'to_mail@gmail.com'
login = os.getenv("EMAIL_LOGIN")
password = os.getenv("EMAIL_PASSWORD")
template = """From: %email_from%
To: %email_to%
Subject: Invite
Content-Type: text/plain; charset="UTF-8";

Добрый день, %friend_name%! %my_name% приглашает посетить тебя сайт %website%!

%website% — это великолепный ресурс. 
"""

replacements_dict = {'%website%': 'mywebsite.org', '%friend_name%': 'Борис', '%my_name%': my_name, '%email_from%': email_from, '%email_to%': email_to}

for keyword, replacement in replacements_dict.items():
    template = template.replace(keyword, replacement)

message = template.encode("UTF-8")

server = smtplib.SMTP_SSL('smtp.google.com:465')
server.login(login, password)
server.sendmail(email_from, email_to, message)
server.quit()
