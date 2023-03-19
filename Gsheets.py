import gspread
from oauth2client.service_account import ServiceAccountCredentials
import json

#connect with Gsheets
scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name('creds.json', scope)
client = gspread.authorize(creds)

# get data from sheets
def get_data():
    sheet = client.open('แจ้งน้ำท่วมซอยตั้งสิน (Responses)').sheet1
    data = sheet.get_all_records()
    latest = data[-1]
    with open('latest.txt', 'r') as file1:
        last_response = file1.read()
        if last_response != str(latest):
            with open ('latest.txt' ,'w') as file2:
                file2.write(str(latest))
            return latest
        else:
            pass

def parse_dict():
    responses = {1 : 'lv1.txt', 2: 'lv2.txt', 3: 'lv3.txt', 4: 'lv4.txt', 5: 'lv5.txt'}
    result = get_data()
    if result:
        resp_tst =result['Timestamp']
        fldprg = open(responses[result['Flood']], 'r').read()
        text = f'Response from {resp_tst} saying {fldprg}'
        return text
            


