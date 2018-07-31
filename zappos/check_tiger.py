import json
import sys
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os.path
import configparser


def read_results(result_file, recipient):
    if not os.path.exists(result_file):
        print("crawled file doesn't exist!")
        exit(1)

    with open(result_file) as f:
        shoes = json.loads(f.read())

    process_results(shoes, recipient)


def process_results(result_list, recipient):
    top_list = result_list[:5]
    send_mail(top_list, "tiger shoes", recipient)


# use gmail
def send_mail(message, title, recipient):
    print("Sending mail to %s" % recipient)

    parser = configparser.ConfigParser()
    parser.read('simple.ini')

    user = parser['DEFAULT']['Username']
    password = parser['DEFAULT']['Password']

    message_str = str(message)

    msg = MIMEMultipart()
    msg['From'] = user
    msg['To'] = recipient
    msg['Subject'] = title
    msg.attach(MIMEText(message_str))

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(user, password)
    server.sendmail(user, recipient, msg.as_string())
    server.close()
    print("Mail sent")


shoes_json_file = sys.argv[1]
recipient = sys.argv[2]
read_results(shoes_json_file, recipient)
