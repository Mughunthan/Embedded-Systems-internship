import os
import machine
from time import sleep
uart = machine.UART(0, 9600)
print(uart)
b = None
msg = ""
while True:
    sleep(0.2)
    print("===========")
    print("hello usb")
    uart.write("hello uart\n")
