from machine import Pin,UART

uart = UART(0,9600)
data=""
data1=""
key="00355217"
while True:
    if uart.any():
        try:
            command = uart.readline()
            data= str(command.decode())
            data1=data1+data
            data1=data1.strip()
            if((len(data1)==8)):
                print(data1)
                if(data1==key):
                    print("key matched")
                else:
                    print("key not matched")
                data1=""
        except:
             pass
      
        