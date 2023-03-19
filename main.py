from Gmailhandler import send_msg
from Tweethandler import post_twt
from Gsheets import parse_dict
import time

while True:
    msg = parse_dict()
    #email part
    recipients = ['urseamlaccs@gmail.com']
    for email in recipients:
        send_msg(email, msg)
    #This is where I'll put my twitter part IF I HAVE ONE >:(
    #post_twt(msg)
    time.sleep(300)
