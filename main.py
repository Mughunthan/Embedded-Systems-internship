# Source: electrocredible.com , Language: MicroPython
# Import necessary modules
from machine import Pin 
import bluetooth
from time import sleep
from ble_simple_peripheral import BLESimplePeripheral

# Create a Bluetooth Low Energy (BLE) object
ble = bluetooth.BLE()
f11=Pin(0,Pin.OUT)
f12=Pin(1,Pin.OUT)
f21=Pin(18,Pin.OUT)
f22=Pin(19,Pin.OUT)
b11=Pin(16,Pin.OUT)
b12=Pin(17,Pin.OUT)
b21=Pin(14,Pin.OUT)
b22=Pin(15,Pin.OUT)

# Create an instance of the BLESimplePeripheral class with the BLE object
sp = BLESimplePeripheral(ble)

# Create a Pin object for the onboard LED, configure it as an output
led = Pin("LED", Pin.OUT)
m=""

# Initialize the LED state to 0 (off)
led_state = 0

def forward():
        f11.value(1)
        f12.value(0)
        f21.value(1)
        f22.value(0)
        b11.value(1)
        b12.value(0)
        b21.value(0)
        b22.value(1)
        sleep(2)
def backward():
        f11.value(0)
        f12.value(1)
        f21.value(0)
        f22.value(1)
        b11.value(0)
        b12.value(1)
        b21.value(1)
        b22.value(0)
        sleep(2)
def rightturn():
        f11.value(0)
        f12.value(0)
        f21.value(1)
        f22.value(0)
        b11.value(1)
        b12.value(0)
        b21.value(0)
        b22.value(1)
        sleep(2)
def leftturn():
        f11.value(1)
        f12.value(0)
        f21.value(0)
        f22.value(0)
        b11.value(1)
        b12.value(0)
        b21.value(0)
        b22.value(1)
        sleep(2)
def stop():
        f11.value(0)
        f12.value(0)
        f21.value(0)
        f22.value(0)
        b11.value(0)
        b12.value(0)
        b21.value(0)
        b22.value(0)
        sleep(2)
def leftback():
        f11.value(0)
        f12.value(0)
        f21.value(0)
        f22.value(1)
        b11.value(0)
        b12.value(1)
        b21.value(1)
        b22.value(0)
        sleep(2)
def rightback():
        f11.value(0)
        f12.value(1)
        f21.value(0)
        f22.value(0)
        b11.value(0)
        b12.value(1)
        b21.value(1)
        b22.value(0)
        sleep(2)
    
# Define a callback function to handle received data
def on_rx(data):
    print("Data received: ", data)  # Print the received data
    global led_state  # Access the global variable led_state
    m=str(data.decode())
    m=m.strip()
    print(m)
    
    if m== 'f':
            forward()
#             lcd.move_to(10,0) 
#             lcd.putstr("FRONT")
            print("FORWARD")
           
    elif m== 'b':
            backward()
#             lcd.move_to(10,0) 
#             lcd.putstr("BACK ")
            print("BACKWARD")
           
    elif m== 'r':
            rightturn()
#             lcd.move_to(10,0) 
#             lcd.putstr("RIGHT")
            print("RIGHT")
            
    elif m== 'l':
            leftturn()
#             lcd.move_to(10,0) 
#             lcd.putstr("LEFT ")
            print("LEFT")
            
    elif m== '2':
            rightback()
#             lcd.move_to(10,0) 
#             lcd.putstr("LB   ")
            print("LEFTBACK")
           
    elif m== '1':
            leftback()
#             lcd.move_to(10,0) 
#             lcd.putstr("RB   ")
            print("RIGHTBACK")
            
    elif m== 's':
            stop()
#             lcd.move_to(10,0) 
#             lcd.putstr("STOP ")
            print("STOP")
    sleep(0.1)

     
# Start an infinite loop
while True:
    if sp.is_connected():  # Check if a BLE connection is established
        #sp.send("data \r \n")
        
        sleep(0.1)
        sp.on_write(on_rx)# Set the callback function for data reception
        
