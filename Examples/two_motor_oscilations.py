import serial
import time


# Functions
def read():
    ser.readline().decode()


ser = serial.Serial("/dev/tty.usbmodem14101")    # open serial port
time.sleep(1)
print(ser.name)         # check which port was really used

# Set Max Speed
ser.write("0,M,250\r\n".encode())
ser.write("1,M,220\r\n".encode())

# Read Max Speed
ser.write("0,M\r\n".encode())
print("Max speed of Motor 0 :", ser.readline().decode())
ser.write("1,M\r\n".encode())
print("Max speed of Motor 1 :", ser.readline().decode())

# Read Position
ser.write("0,P\r\n".encode())
print("Position of Motor 0 :", ser.readline().decode())
ser.write("1,P\r\n".encode())
print("Position of Motor 1 :", ser.readline().decode())

# Write Position 0
ser.write("0,P,0\r\n".encode())
ser.write("1,P,0\r\n".encode())

ser.close()  # close port
