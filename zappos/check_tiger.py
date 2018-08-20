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


def convert_to_html_str(list):
    # construct brand header row
    header_str = ''
    for item in list:
        header_str += '<tr>'
        for key in item.keys():
            header_str += '<th>'
            header_str += key
            header_str += '</th>'
        header_str += '</tr>'
        break

    # construct content table rows
    row_str = ''
    for row_item in list:
        row_str += '<tr>'
        for (key, value) in row_item.items():
            if key == 'photo_src':
                row_str += '<img src="{}">'.format(value)
            else:
                row_str += '<td>'
                row_str += value
                row_str += '</td>'
        row_str += '</tr>'

    # construct table
    table_str = '<table>'
    table_str += header_str
    table_str += row_str
    table_str += '</table>'

    return table_str


def process_results(result_list, recipient):
    top_list = result_list[:5]
    html_str = convert_to_html_str(top_list)
    send_mail(html_str, "tiger shoes", recipient)


# use gmail
def send_mail(message, title, recipient):
    print("Sending mail to %s" % recipient)

    parser = configparser.ConfigParser()
    parser.read('simple.ini')

    user = parser['DEFAULT']['Username']
    password = parser['DEFAULT']['Password']

    msg = MIMEMultipart()
    msg['From'] = user
    msg['To'] = recipient
    msg['Subject'] = title
    msg.attach(MIMEText(message, 'html'))

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
