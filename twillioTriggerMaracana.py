from twilio.rest import Client # type: ignore
import os

account_sid = os.getenv("ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")
client = Client(account_sid, auth_token)

def sendTheMessage(mensagem):
    message = client.messages.create(
    body=mensagem,
    from_='whatsapp:+14155238886',
    to=f'whatsapp:{os.getenv("USER_TEL")}'
    )
    print(message.sid)
    print(message.body)
