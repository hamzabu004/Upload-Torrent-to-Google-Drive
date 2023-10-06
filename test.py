from twilio.rest import Client
from googlesearch import search

# Your Account SID from twilio.com/console
account_sid = ""
# Your Auth Token from twilio.com/console
auth_token  = ""

client = Client(account_sid, auth_token)
result = "Torrent Completed."

message = client.messages \
      .create(
          body=result,
          from_='whatsapp:+14155238886',
          to='whatsapp:+923081354838'
      )

print(message.sid)