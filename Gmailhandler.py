from Google import create_service
import base64
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from Gsheets import parse_dict
import time



def gen_service():
    CLIENT_SECRET_FILE = 'creds_gmail.json'
    APP_NAME = 'gmail'
    API_VERSION = 'v1'
    SCOPES = ['https://mail.google.com/']

    service = create_service(CLIENT_SECRET_FILE, APP_NAME, API_VERSION, SCOPES)
    return service

def send_msg(recipient, msg = None, service = None):
    if service:
        pass
    else:
        service = gen_service()
    emailMsg = msg
    if emailMsg:
        mimeMessage = MIMEMultipart()
        mimeMessage['to'] = recipient
        mimeMessage['subject'] = '(Automated Message) Report on the flooding situation'
        mimeMessage.attach(MIMEText(emailMsg, 'plain', _charset='UTF-8'))
        raw_string = base64.urlsafe_b64encode(mimeMessage.as_bytes()).decode()
        message = service.users().messages().send(userId='me', body={'raw': raw_string}).execute()
    time.sleep(3000)    
    #print(message)