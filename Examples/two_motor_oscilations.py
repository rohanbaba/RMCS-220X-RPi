import serial
import time

ser = serial.Serial("/dev/tty.usbmodem14101")    # open serial port
time.sleep(1)
print("Port :", ser.name)         # check which port was really used


# Functions
def read():
    return ser.readline().decode()


# Read Position
ser.write("0,P\r\n".encode())
print("Max speed of Motor 0 (before turning):", read())
ser.write("1,P\r\n".encode())
print("Max speed of Motor 1 (before turning):", read())


# Go To 1800
ser.write("0,G,100\r\n".encode())
ser.write("1,G,100\r\n".encode())

# Read Position
ser.write("0,P\r\n".encode())
print("Max speed of Motor 0 (after turning):", read())
ser.write("1,P\r\n".encode())
print("Max speed of Motor 1 (after turning):", read())

ser.close()  # close port
