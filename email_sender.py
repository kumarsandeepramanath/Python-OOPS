import smtplib
from email.message import EmailMessage

email = EmailMessage()
email['from'] = "Sandeep with Python"
email['to'] = 'ksandeepr89@gmail.com'
email['subject'] = 'Testing of sending emails'
email.set_content("I am a Python Master")

with smtplib.SMTP(host='smtp.gmail.com',port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('ksandeepr89@gmail.com','Chatbot*1989')
    smtp.send_message(email)
    print('all good boss!!')