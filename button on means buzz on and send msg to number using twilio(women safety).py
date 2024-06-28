#twiliosms.py
try:
  import urequests as requests
except:
  import requests
  
import network
import gc
from  machine import Pin
import time
 
b=Pin(4,Pin.IN)
buz=Pin(6,Pin.OUT)
 
ssid = 'Project'
password = '12345678'
flag=0

# Your Account SID and Auth Token from twilio.com/console
account_sid = 'AC06bbe6e233df438d77cf13d3385fbb83'
auth_token = 'a9250d2b050eef906985dd34a48651c5'
recipient_num = '+917200030070'
sender_num = '+12057513481'

def send_sms(recipient, sender,
             message, auth_token, account_sid):
    flag=1 
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    data = "To={}&From={}&Body={}".format(recipient,sender,message)
    url = "https://api.twilio.com/2010-04-01/Accounts/{}/Messages.json".format(account_sid)
    
    print("Trying to send SMS with Twilio")
    
    response = requests.post(url,
                             data=data,
                             auth=(account_sid,auth_token),
                             headers=headers)
    
    if response.status_code == 201:
        print("SMS sent!")
    else:
        print("Error sending SMS: {}".format(response.text))
    
    response.close()

def connect_wifi(ssid, password):
  
  station = network.WLAN(network.STA_IF)
  station.active(True)
  station.connect(ssid, password)
  while station.isconnected() == False:
    pass
  print('Connection successful')
  print(station.ifconfig())

connect_wifi(ssid, password)
message = "Help!...help!....save me"
while(1):
 if b.value()==0 and flag==0:
    buz.on()
    send_sms(recipient_num, sender_num, message, auth_token, account_sid)
 time.sleep(0.1)