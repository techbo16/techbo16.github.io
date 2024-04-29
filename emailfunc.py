import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(full_name, email, message, recipient_email):
    # Email configurations
    sender_email = 'derek@osaitechsolutions.com'  # Replace with your email
    sender_password = 'Superfly2020!'  # Replace with your password
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587

    # Create message
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = 'OSAI TECH SOlUTIONS'

    body = f"Full Name: {full_name}\nEmail: {email}\nMessage: {message}"
    msg.attach(MIMEText(body, 'plain'))

    # Send the message via SMTP server
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, recipient_email, msg.as_string())

# Example usage
if __name__ == "__main__":
    full_name = input("Enter your full name: ")
    email = input("Enter your email address: ")
    message = input("Enter your message: ")
    recipient_email = input("Enter recipient's email address: ")

    send_email(full_name, email, message, recipient_email)

