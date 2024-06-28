#udp_send.py
import network
import socket
import time
from machine import Pin,ADC
from time import sleep
pot=ADC(28)
cv=3300/65535
pot1=ADC(27)    #temperature sensor(LM 35)


wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect("moto g40","00000000")
 
#remote port
UDP_IP = "192.168.134.148"
UDP_PORT = 1234
MESSAGE = "Hello, World!"
 
# Wait for connect or fail
wait = 10
while wait > 0:
    if wlan.status() < 0 or wlan.status() >= 3:
        break
    wait -= 1
    print('waiting for connection...')
    time.sleep(1)
 
# Handle connection error
if wlan.status() != 3:
    raise RuntimeError('wifi connection failed')
else:
    print('connected')
    ip=wlan.ifconfig()[0]
    print('IP: ', ip)
 
    
localIP  = wlan.ifconfig()[0]
localPort   = 1234
bufferSize  = 1024

# Create a datagram socket
UDPServerSocket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)


# Bind to address and ip
UDPServerSocket.bind((localIP, localPort))
print('waiting....')

while True:
    #data send
    temp=int(pot1.read_u16()*cv/10)
    potv=int(pot.read_u16()*cv)
    sleep(0.2)
    m=str(temp)+","+str(potv)
    print(m)
    UDPServerSocket.sendto(m.encode(), (UDP_IP, UDP_PORT))
    time.sleep(2)