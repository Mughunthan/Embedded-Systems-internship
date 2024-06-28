from machine import Pin,ADC
from time import sleep

POT_Value = ADC(28)

def map_value(in_v, in_min, in_max, out_min, out_max): #v=value
    v = (in_v - in_min) * (out_max - out_min) / (in_max - in_min) + out_min  #inmin=0,inmax=65535
    if v < out_min:       #outmin=0,outmax=100
        v = out_min
    elif v > out_max:
        v = out_max
    return v

while(1):
    value = POT_Value.read_u16()
    m=int(map_value(value,65535,25535,0,100))
    print(m)
    sleep(0.5)