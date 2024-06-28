from time import sleep

from machine import Pin

from machine import PWM

pwm = PWM(Pin(28))

pwm.freq(50)

def setServoCycle (position):

    pwm.duty_u16(position)

    sleep(0.01)

while True:

    for pos in range(1000,9000,200):

        setServoCycle(pos)

    for pos in range(9000,1000,-200):

        setServoCycle(pos)