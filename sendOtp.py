import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def sendEmail(receiver_email,otp):
    sender_email = "shayan851997@outlook.com"
    subject = "OTP Verfication"
    body = "Your OTP is : " + str(otp)

    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = receiver_email
    message['Subject'] = subject
    message.attach(MIMEText(body, 'plain'))

    smtp_server = "smtp-mail.outlook.com"
    smtp_port = 587 

    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender_email, "Shayan97@")

        text = message.as_string()
        server.sendmail(sender_email, receiver_email, text)
        print("Email sent successfully!")

    except Exception as e:
        print(f"An error occurred: {str(e)}")

    finally:
        server.quit()