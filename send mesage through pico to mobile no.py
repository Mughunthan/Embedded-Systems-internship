from machine import Pin,UART
from time import sleep
import utime

tx_pin = machine.Pin(0)
rx_pin = machine.Pin(1)
uart = machine.UART(0, baudrate=9600, tx=tx_pin, rx=rx_pin)

response = b''

init='AT\r\n' #TO CHECK MODULE 

sms_txt='AT+CMGF=1\r\n' #Text mode to send a Short Message 

sms_to='AT+CMGS="+919042591157"\r\n' #read newly arrived message

message="Hello, world!"

end=bytes([0x1A]) #Ctrl+Z character to indicate the end of the message

def CHK():
    global response
    start_time = utime.ticks_ms()
    while utime.ticks_diff(utime.ticks_ms(), start_time) < 1000:
        if uart.any():
            response += uart.read(1)
    print(response)
    #response=""

uart.write(init)
CHK()
sleep(0.5)
uart.write(sms_txt)
CHK()
sleep(0.5)
uart.write(sms_to) 
CHK()
uart.write(message)
CHK()
uart.write(end)
while(1):
    CHK()