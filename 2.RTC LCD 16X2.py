from machine import mem32,Pin
from time import sleep_ms 
b0=Pin(0,Pin.IN,Pin.PULL_UP)
b1=Pin(1,Pin.IN,Pin.PULL_UP)
b2=Pin(2,Pin.IN,Pin.PULL_UP)
b3=Pin(3,Pin.IN,Pin.PULL_UP)
b4=Pin(4,Pin.IN,Pin.PULL_UP)
b5=Pin(5,Pin.IN,Pin.PULL_UP)
b6=Pin(6,Pin.IN,Pin.PULL_UP)
b7=Pin(7,Pin.IN,Pin.PULL_UP)
addrSIO = 0xd0000000
while True:
    value=mem32[addrSIO + 0x004]
    print(bin(value))
    sleep_ms(500)