#udp_sen_rec.py
import network
import socket
import time

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect("moto g40","00000000")
 
#remote port
UDP_IP = ""
UDP_PORT = 1265
MESSAGE = ""
 
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
    #receive
    bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)
    message = bytesAddressPair[0]
    address = bytesAddressPair[1]
    UDP_IP=address[0]
    print(address[0])
    print(message)
    m=input("ur name:")
    #data send
    UDPServerSocket.sendto(m.encode(), (UDP_IP, UDP_PORT))

    time.sleep(2)

