from machine import Pin
import network
import socket
import time
led=Pin(2,Pin.OUT)
led2=Pin(3,Pin.OUT)

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect("moto g40","00000000")
 
# # rgb led
# led1=machine.Pin(2,machine.Pin.OUT)
# led2=machine.Pin(3,machine.Pin.OUT)

 
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
    bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)
    print(bytesAddressPair)
    message = bytesAddressPair[0]
    address = bytesAddressPair[1]
    m=str(message.decode())
    m=m.strip()
    if(m=="1"):
        led.on()
        led2.off()
    if(m=="2"):
        led2.on()
        led.off()
    print(m)

