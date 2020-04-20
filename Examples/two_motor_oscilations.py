import serial
import time

ser = serial.Serial("/dev/tty.usbmodem14101")    # open serial port
time.sleep(1)
print("Port :", ser.name)         # check which port was really used


# Functions
def read():
    return ser.readline().decode()


# Max Speed to 250
ser.write("0,M,240\r\n".encode())
print("Max Speed of Motor 0 :", read())
ser.write("1,M,240\r\n".encode())
print("Max Speed of of Motor 1 :", read())

# Current Position to 0
ser.write("0,P,0\r\n".encode())
print(read())
ser.write("1,P,0\r\n".encode())
print(read())

while True:

    # Read Position
    ser.write("0,P\r\n".encode())
    print("Position of Motor 0 :", read())
    ser.write("1,P\r\n".encode())
    print("Position of Motor 1 :", read())

    time.sleep(0.1)

    # Go To 1800 steps
    ser.write("0,G,500\r\n".encode())
    ser.write("1,G,500\r\n".encode())

    time.sleep(3)

    # Read Position
    ser.write("0,P\r\n".encode())
    print("Position of Motor 0 :", read())
    ser.write("1,P\r\n".encode())
    print("Position of Motor 1 :", read())

    time.sleep(0.1)

    # Go To 0 steps
    ser.write("0,G,0\r\n".encode())
    ser.write("1,G,0\r\n".encode())

    time.sleep(3)

    print("Next Loop")
