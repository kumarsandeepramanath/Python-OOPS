# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'AC4645328daba645ba20bc8c3378eeb2f5'
auth_token = '3759e0e75813dad3b489f40007dc2725'
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="Join Earth's mightiest heroes. Welcome to the world of Python.",
                     from_='+12185162782',
                     to='+91 99016 63922'
                 )

print(message.sid)
