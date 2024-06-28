#moisture in phone call/sms 
from machine import Pin,UART
from time import sleep
import utime
import network
import gc 
from machine import Pin,ADC
from time import sleep

moisture = ADC(28)
flag=0
flag1=0
tx_pin = Pin(0)
rx_pin = Pin(1)
uart = UART(0, baudrate=9600, tx=tx_pin, rx=rx_pin)

response = b''
init='AT\r\n'
call='ATD+917200030070;\r\n' #make call
end_call='ATH\r\n' #make cali
sms_txt='AT+CMGF=1\r\n' #Text mode to send a Short Message 
sms_to='AT+CMGS="+917200030070"\r\n' #read newly arrived message
message_low="nothing to fear"
message_high="water level high in soil"
end=bytes([0x1A]) #Ctrl+Z character to indicate the end of the message

def map_value(in_v, in_min, in_max, out_min, out_max): #v=value
    v = (in_v - in_min) * (out_max - out_min) / (in_max - in_min) + out_min  #inmin=0,inmax=65535
    if v < out_min:       #outmin=0,outmax=100
        v = out_min
    elif v > out_max:
        v = out_max
    return v

while(1):
    value = moisture.read_u16()
    m=int(map_value(value,65535,25535,0,100))
    print(m)
    sleep(0.5)
    
    if m>=85:
       print(message_high)
       if(flag==0):
           print("sms sent high")
           sleep(3)
           uart.write(sms_txt)
           sleep(0.5)
           uart.write(sms_to)
           sleep(0.5)
           uart.write(message_high)
           sleep(0.5)
           uart.write(end)
           sleep(3)
           uart.write(init)
           sleep(0.5)
           uart.write(call)
           sleep(0.5)
           flag=1
           flag1=0
    elif m<25:
       
       print(message_low)
       if(flag1==0):
          print("sms sent low")
          sleep(3)
          uart.write(sms_txt)
          sleep(0.5)
          uart.write(sms_to)
          sleep(0.5)
          uart.write(message_low)
          sleep(0.5)
          uart.write(end)
          sleep(0.5)
          flag=0
          flag1=1 
     
       
    

