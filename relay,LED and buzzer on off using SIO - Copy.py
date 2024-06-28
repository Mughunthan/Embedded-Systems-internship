
from machine import mem32,Pin
from time import sleep_ms 
led1=Pin(2,Pin.OUT)
led2=Pin(3,Pin.OUT)
b=Pin(6,Pin.OUT)
r=Pin(7,Pin.OUT)

addrSIO = 0xd0000000
while True:
    mem32[addrSIO + 0x014] = 0x000000cc
    sleep_ms(500)
    mem32[addrSIO + 0x018] = 0x000000cc
    sleep_ms(500)

