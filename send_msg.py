import os
from twilio.rest import Client
from dotenv import load_dotenv
load_dotenv()
auth_token = os.environ['TWILIO_AUTH_TOKEN']
account_sid = os.environ['TWILIO_ACCOUNT_SID']
client = Client(account_sid, auth_token)

twilio_default_number = "whatsapp:+14155238886"
twilio_to = "whatsapp:+59174361042"

def send_msg(msg_from_whatsapp):
  message = client.messages.create(
    body=msg_from_whatsapp,
    from_=twilio_default_number,
    to=twilio_to
  )
  print(message)
  return message

