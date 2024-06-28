import os
import machine
from time import sleep
from machine import Pin,ADC

led=Pin(2,Pin.OUT)
pvalue=machine.ADC(28)
uart = machine.UART(0, 9600)
print(uart)
b = None
msg = ""
while True:
    sleep(1)
    pread=pvalue.read_u16()
    
    level= int(100-(pread*(100/65535)))
    #print("water content in soil:",level)


    uart.write(str(level))
    if uart.any():
         command = uart.readline()
         data=str(command.decode())
         print(data)
         if data=="on":
             led.on()
         elif data=="off":
             led.off()
         else:
             print("")
             
    
