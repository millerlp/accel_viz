# Kairi Yoon Tezuka
# 08/12/2016

# Arduino Uno LSM303 Accelerometer/Magnetometer/Compass
# Arudiono to Python real-time serial port data

# below is how the serial port input is read
# compass.a.x, compass.a.y, compass.a.z, compass.m.x, compass.m.y, compass.m.z
# /dev/cu.usbmodem1421

import serial, time
ser = serial.Serial('/dev/cu.usbmodem1421', 57600)
while 1:
    serial_line=ser.readline()
    print serial_line
    time.sleep(10)
