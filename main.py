import requests
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# API Key and email details
API_KEY = os.getenv("ELASTICEMAIL_API_KEY")
EMAIL_SENDER = os.getenv("EMAIL_SENDER")
EMAIL_RECIPIENTS = os.getenv("EMAIL_RECIPIENTS").split(',')

# Fungsi untuk mengirim email
def send_email(to_email, subject, message):
    url = 'https://api.elasticemail.com/v2/email/send'
    payload = {
        'apikey': API_KEY,
        'from': EMAIL_SENDER,
        'to': to_email,
        'subject': subject,
        'bodyText': message,
    }
    
    response = requests.post(url, data=payload)
    
    if response.status_code == 200:
        print(f"Email sent to {to_email}")
    else:
        print(f"Failed to send email to {to_email}: {response.text}")

# Fungsi untuk mengirim broadcast email ke semua penerima
def send_broadcast(subject, message):
    for recipient in EMAIL_RECIPIENTS:
        send_email(recipient, subject, message)

# Subject dan pesan email
subject = 'Pengumuman Penting'
message = 'Ini adalah pesan broadcast yang dikirim menggunakan Elastic Email dan Railway.'

# Kirim broadcast email
send_broadcast(subject, message)
