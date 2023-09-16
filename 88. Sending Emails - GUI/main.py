import smtplib      # import simple mail transfer protocol library

sender = "yulansenula179@gmail.com"
receiver = "yulangalagodaofficial@gmail.com"
password = "2987529875"
subject = "Python Email Test"
body = "I sent this with a python program I wrote!!!!"

# header
message = f"""
From: Yulan{sender}
To: Senula{receiver}
Subject: {subject}\n
{body}
"""

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login(sender, password)
print("Logged In")

server.sendmail(sender, receiver, message)
print("Email has been sent!")
