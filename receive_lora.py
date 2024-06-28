from machine import Pin,UART
from time import sleep
sw1=Pin(4,Pin.IN)
uart = UART(0,9600)
ON="on"
OFF="off"
flag=0
while True:
    b=sw1.value()
    if b==0:
        flag=not(flag)
        sleep(0.5)
    else:
        flag=flag
        sleep(0.5)
    if flag==1:
        uart.write(str(ON))
        print(ON)
        sleep(0.5)
        
    else:
        uart.write(str(OFF))
        print(OFF)
        sleep(0.5)
    if uart.any():
         command = uart.readline()
         data=str(command.decode())
         n=len(data)
         if(n<=2):
             print("the water content in soil:",data)
         else:
             print("")
    sleep(0.5)
        