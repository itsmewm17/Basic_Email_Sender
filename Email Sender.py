from email.message import EmailMessage 
#from app2 import password  #輸入你取得的pw  ，影片沒有講app2內容是什麼....
import ssl
import smtplib

email_sender = "alvin.bskproductions@gmail.com"
email_password = "" 

email_receiver ="alvin.bskproductions@gmail.com"  

subject = "Don't Ever Try to Peek at the Content"
body= """
It's just a joke.
"""

em = EmailMessage ()
em ["From"] = email_sender
em ["To"] = email_receiver
em ["subject"] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())