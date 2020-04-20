import serial
import time

ser = serial.Serial("/dev/tty.usbmodem14101")    # open serial port
time.sleep(1)
print("Port :", ser.name)         # check which port was really used


# Functions
def read():
    return ser.readline().decode()


# Max Speed to 250
ser.write("0,M,250\r\n".encode())
ser.write("1,M,250\r\n".encode())

# Read Position
ser.write("0,P\r\n".encode())
print("Position of Motor 0 (before turning):", read())
ser.write("1,P\r\n".encode())
print("Position of Motor 1 (before turning):", read())

# Go To 1800
ser.write("0,G,0\r\n".encode())
ser.write("1,G,0\r\n".encode())

time.sleep(10)

# Read Position
ser.write("0,P\r\n".encode())
print("Position of Motor 0 (after turning):", read())
ser.write("1,P\r\n".encode())
print("Position of Motor 1 (after turning):", read())

ser.close()  # close port
