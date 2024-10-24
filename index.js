// Import dependencies
const elasticemail = require('elasticemail');
require('dotenv').config();

// Inisialisasi Elastic Email Client dengan API Key dari .env
const client = elasticemail.createClient({
  apiKey: process.env.ELASTICEMAIL_API_KEY,
});

// Fungsi untuk mengirim email individual
const sendEmail = (toEmail, subject, message) => {
  const emailParams = {
    from: process.env.EMAIL_SENDER,  // Ambil email pengirim dari .env
    to: toEmail,
    subject: subject,
    bodyText: message,
  };

  client.mailer.send(emailParams, function (err, res) {
    if (err) {
      console.error(`Error sending to ${toEmail}:`, err);
    } else {
      console.log(`Email sent to ${toEmail}:`, res);
    }
  });
};

// Fungsi untuk mengirim email ke banyak penerima (broadcast)
const sendBroadcast = (recipients, subject, message) => {
  recipients.forEach((recipient) => {
    sendEmail(recipient, subject, message);
  });
};

// Ambil penerima dari variabel lingkungan dan pisahkan berdasarkan koma
const recipients = process.env.EMAIL_RECIPIENTS.split(',');

// Subjek dan pesan email
const subject = 'Pengumuman Penting';
const message = 'Ini adalah pesan broadcast yang dikirim menggunakan Elastic Email dan Railway.';

// Kirim broadcast email ke seluruh penerima
sendBroadcast(recipients, subject, message);
