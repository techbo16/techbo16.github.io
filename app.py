from flask import Flask, render_template, request
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import random

app = Flask(__name__)

# List of potential recipients
recipient_emails = ['recipient1@example.com', 'recipient2@example.com', 'recipient3@example.com']

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send_email', methods=['POST'])
def send_email():
    if request.method == 'POST':
        full_name = request.form['full_name']
        email = request.form['email']
        message = request.form['message']
        
        sender_email = 'derek@osaitechsolutions.com'  # Replace with your email
        sender_password = 'Superfly2020!'  # Replace with your password
        
        # Select a random recipient from the list
        recipient_email = random.choice(recipient_emails)

        # Create message
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = recipient_email
        msg['Subject'] = 'Message from Contact Form'

        body = f"Full Name: {full_name}\nEmail: {email}\nMessage: {message}"
        msg.attach(MIMEText(body, 'plain'))

        # Send the message via SMTP server
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, recipient_email, msg.as_string())

        return "Email sent successfully!"

if __name__ == '__main__':
    app.run(debug=True)
