from twilio.rest import Client

# Twilio credentials
account_sid = "AC5672c32dedffb20dfc764461a297690e"
auth_token = "f9c6fc2a79443a3912b8c841f914f276"
twilio_phone_number = "+14155238886"  # Use a valid Twilio phone number enabled for WhatsApp

# Destination WhatsApp number in E.164 format
to_whatsapp_number = "+918122992143"  # Replace with a valid WhatsApp number

# Create Twilio client
client = Client(account_sid, auth_token)

# Send WhatsApp message
message = client.messages.create(
    body="Hello, this is a WhatsApp message sent using Twilio and Python!",
    from_=twilio_phone_number,
    to=to_whatsapp_number
)

print(f"WhatsApp message sent with SID: {message.sid}")
