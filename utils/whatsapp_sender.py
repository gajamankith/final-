from twilio.rest import Client

client = Client(
    ACCOUNT_SID,
    AUTH_TOKEN
)

client.messages.create(
    body=f"Package Arrived. Tracking ID: {tracking_id}",
    from_='whatsapp:+14155238886',
    to=f'whatsapp:{student_phone}'
)