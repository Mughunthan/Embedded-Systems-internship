# firebase_control.py
from machine import Pin, ADC, UART        
from time import sleep
import socket
import utime
import network
import urequests
import _thread
import ufirebase as firebase
#https://mughuntha-a7e7b-default-rtdb.firebaseio.com/FirebaseIOT
firebase.setURL("https://mughuntha-a7e7b-default-rtdb.firebaseio.com/")

 
uart = UART(0,9600)
data=""
data1=""
key="00343231"
key1="00355217"


ssid = 'Project'
password = '12345678'
 
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(ssid, password)

wait = 10
while wait > 0:
    if wlan.status() < 0 or wlan.status() >= 3:
        break
    wait -= 1
    print('waiting for connection...')
    sleep(1)
  

# Handle connection error
if wlan.status() != 3:
    raise RuntimeError('network connection failed')
    lcd.move_to(0,0) 
    lcd.putstr("WiFi Not Connected")
    sleep(2)
    lcd.clear()
else:
    print('connected')
    status = wlan.ifconfig()
    print( 'ip = ' + status[0] )

    sleep(2)  

while True:
    if uart.any():
        try:
            command = uart.readline()
            data= str(command.decode())
            print(data)
            data1=data1+data    #used to add single bit of data
            data1=data1.strip()
            if((len(data1)==8)):
                print(data1)
                if(data1==key):
                    name="mughuntha"
                    RFID=str(data1)
                    print("put")
                    firebase.put("RFID1/ID",RFID ,bg=0, id=3)
                    firebase.put("RFID1/name",name ,bg=0, id=3)
                    print("key matched")
                    m=str(RFID)+","+str(name)
                    print(m)
                    print("ok")
#                     print(m)
#                     UDPServerSocket.sendto(m.encode(), (UDP_IP, UDP_PORT))
                elif(data1==key1):
                    name2="mughu"
                    RFID2=str(data1)
                    firebase.put("RFID2/ID",RFID2,bg=0, id=3)
                    firebase.put("RFID2/name",name2 ,bg=0, id=3)
                    print("key matched")
                    m2=str(RFID2)+","+str(name2)
                    print(m2)
                    print("ok")
                    #UDPServerSocket.sendto(m.encode(), (UDP_IP, UDP_PORT))
                    
                else:
                    print("key not matched")
                data1=""  # again we are empty this
        except:
             pass
      
    
 

    
     
