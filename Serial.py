import serial
import time

ser = serial.Serial("/dev/tty.usbmodem14101")    # open serial port
time.sleep(1)
print(ser.name)         # check which port was really used


# Functions
def cmd(command):
    command_str = command + "\r\n"
    return ser.write(command_str.encode())


def read():
    return ser.readline().decode()


# Set Max Speed
ser.write(cmd("0,M,200"))
ser.write("1,M,220\r\n".encode())

# Read Max Speed
ser.write("0,M\r\n".encode())
print("Max speed of Motor 0 :", read())
ser.write("1,M\r\n".encode())
print("Max speed of Motor 1 :", ser.readline().decode())

ser.close()  # close port
