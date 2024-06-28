# firebase_control.py
from machine import Pin, ADC        
import time 
import utime
import network
import urequests
import _thread
import ufirebase as firebase

firebase.setURL("https://mughuntha-a7e7b-default-rtdb.firebaseio.com/")

led=Pin("LED",Pin.OUT) #7
led.low()


ssid = 'Redmi'
password = 'kbnithish'
 
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(ssid, password)

wait = 10
while wait > 0:
    if wlan.status() < 0 or wlan.status() >= 3:
        break
    wait -= 1
    print('waiting for connection...')
   

    time.sleep(1)
  

# Handle connection error
if wlan.status() != 3:
    raise RuntimeError('network connection failed')
    lcd.move_to(0,0) 
    lcd.putstr("WiFi Not Connected")
    time.sleep(2)
    lcd.clear()
else:
    print('connected')
    status = wlan.ifconfig()
    print( 'ip = ' + status[0] )

    time.sleep(2)

    #lcd.clear()  


while True:
    time.sleep(3)
    print("put")
    temperature = str(30)
    firebase.put("FirebaseIOT/temperature", temperature, bg=0, id=3)
    print("get")
    #get data from fb
    firebase.get("FirebaseIOT", "led", bg=0, id=0)
    words=firebase.led 
    d=words['led']
    direct=str(d)
    print(direct)
   # print(type(direct))
    if(direct=="1"):
        led.high()
    if(direct=="0"):
        led.low()