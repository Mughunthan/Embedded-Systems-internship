import socket
import xlwt 
from xlwt import Workbook
from datetime import datetime
UDP_IP = "0.0.0.0"  # Listen on all available interfaces
UDP_PORT = 1234     # Choose an available port number

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to the specified IP address and port
sock.bind((UDP_IP, UDP_PORT))

print(f"Listening for UDP packets on {UDP_IP}:{UDP_PORT}")
wb = Workbook() 
sheet1 = wb.add_sheet('Sheet 1')
sheet1.write(0, 0, 'SNO') 
sheet1.write(0, 1, 'DATE_TIME') 
sheet1.write(0, 2, 'VR_VA') 
sheet1.write(0, 3, 'VY_VF') 
sheet1.write(0, 4, 'VB') 
sheet1.write(0, 5, 'TORQUE') 
sheet1.write(0, 6, 'PIN') 
sheet1.write(0, 7, 'LB') 
sheet1.write(0, 8, 'RPM') 
sheet1.write(0, 9, 'LR_LA')
sheet1.write(0, 10, 'LY_LF') 
sheet1.write(0, 11, 'PF_DEG') 
sheet1.write(0, 12, 'POUT') 
sheet1.write(0, 13, 'EFFICIENCY') 
sheet1.write(0, 14, 'POWER')
sheet1.write(0, 15, 'G') 
sheet1.write(0, 16, 'SPEED')

now = datetime.now()
file_string = now.strftime('%Y-%m-%d %H:%M:%S')
file_string=file_string.replace(" ","_")
file_string=file_string.replace(":","_")
file_string=file_string.replace("-","_")
wb.save(str(file_string)+'.xls') 

row=1
sno=1

while True:
    # Receive data and address from the socket
    data, addr = sock.recvfrom(1024)  # Adjust the buffer size as needed
    m=data.decode()
    data = m.split(',')
    d1=data[0]
    d2=data[1]
    print(m)
    dt = datetime.now()
    dtstring = dt.strftime('%Y-%m-%d %H:%M:%S')
    for col in range(1):
        if col==0:
            sheet1.write(row,col,str(sno))
        elif col==1:
            sheet1.write(row,col,str(dtstring))
    sno=sno+1
    row=row+1
    wb.save(str(file_string)+'.xls')
    # Print received data and sender's address
    #print(f"Received message: {data.decode('utf-8')} from {addr}")
