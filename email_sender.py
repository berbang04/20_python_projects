from email.message import EmailMessage
import ssl
import smtplib

email_sender='selimbirgul39@gmail.com'
email_password='hvlipqqtpusizlfi'

email_receiver='veyselsayar6@gmail.com'

subject='python task denedim'

body="""
email sender baya iyi bir şey denemeni tavsiye ederim veyselcim
"""

em=EmailMessage()
em['From']=email_sender
em['To']=email_receiver
em['subject']=subject
em.set_content(body)

context=ssl.create_default_context()
with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as server:
    server.login(email_sender,email_password)
    server.sendmail(email_sender,email_receiver,em.as_string())