import requests
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# API Key and email details from environment variables
API_KEY = os.getenv("ELASTICEMAIL_API_KEY")
EMAIL_SENDER = os.getenv("EMAIL_SENDER")
EMAIL_RECIPIENT = os.getenv("EMAIL_RECIPIENT_TEST")  # Email tes untuk memastikan koneksi

# Fungsi untuk menguji koneksi ke Elastic Email API
def test_elastic_email_connection():
    # Subject dan pesan email sederhana untuk tes
    subject = "Tes Koneksi Elastic Email"
    message = "Jika Anda menerima email ini, koneksi ke Elastic Email API berhasil!"
    
    # URL endpoint untuk mengirim email menggunakan Elastic Email API
    url = 'https://api.elasticemail.com/v2/email/send'
    
    # Payload berisi data email
    payload = {
        'apikey': API_KEY,
        'from': EMAIL_SENDER,
        'to': EMAIL_RECIPIENT,
        'subject': subject,
        'bodyText': message,
    }

    try:
        # Kirim request POST ke Elastic Email API
        response = requests.post(url, data=payload)
        
        # Periksa status response
        if response.status_code == 200:
            print(f"Tes berhasil! Email dikirim ke {EMAIL_RECIPIENT}")
        else:
            print(f"Tes gagal! Status Code: {response.status_code}")
            print(f"Response: {response.text}")
    except Exception as e:
        print(f"Error saat mencoba menghubungi Elastic Email API: {e}")

# Jalankan fungsi tes
test_elastic_email_connection()
