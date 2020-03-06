from twilio.rest import Client


account_sid = ''
auth_token = ''
client = Client(account_sid, auth_token)

message = client.messages.create(
    from_='+12055707564',
    body='Test message',
    to='+306991234567'
)

print(message.sid)

exit()