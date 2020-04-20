import serial
import time

ser = serial.Serial("/dev/tty.usbmodem14101")    # open serial port
time.sleep(1)
print(ser.name)         # check which port was really used

# Max Speed
ser.write("0,M,250\r\n".encode())
ser.write("1,M,220\r\n".encode())

ser.write("0,M\r\n".encode())
print("Max speed of Motor 0 :", ser.readline().decode())

ser.write("1,M\r\n".encode())
print("Max speed of Motor 1 :", ser.readline().decode())


ser.close()             # close port
