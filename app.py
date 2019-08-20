from twilio.rest import Client
import config

client = Client(config.account_sid, config.auth_token)

call = client.messages.create(
    to="+50370079032",
    from_="+13523544180",
    body="Hola bello"
)

print(call.price)
print(call.date_sent)