from machine import Pin,UART
from time import sleep
uart = UART(0,9600)
data=""
data1=""
key="00355217"
while True:
    if uart.any():
         command = uart.readline()
         print(command)
    sleep(0.2)
         