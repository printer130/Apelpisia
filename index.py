from bottle import run, post, request, error, get, route
from twilio.twiml.messaging_response import MessagingResponse
from completion import client
from send_msg import send_msg

@get('/')
def first():
  return 'hola'

@route('/hello')
def hello():
    return "Hello World!"

@post('/message')
def reply():
    msg = request.forms.get('Body')
    res = client(msg)
    openai_response_text = send_msg(res)
    response = MessagingResponse()
    response.message(res)
    return str(response)
run(host='localhost', port=8080, debug=True)