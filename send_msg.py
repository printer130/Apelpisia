import os
from twilio.rest import Client
from dotenv import load_dotenv
load_dotenv()
#auth_token = os.environ['TWILIO_AUTH_TOKEN']
#account_sid = os.environ['TWILIO_ACCOUNT_SID']
account_sid = 'ACf941a16c3c982d65b7fc8a19b9869d01'
auth_token = '3230d4b70d679687597d170bb5232d1d'
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

