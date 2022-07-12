import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import numpy as np
import random
import serial
import sys

#initialize serial port
ser = serial.Serial()
ser.port = '/dev/ttyUSB0' if len(sys.argv) == 1 else sys.argv[1] #Arduino serial port
ser.baudrate = 115200
ser.timeout = 10 #specify timeout when using readline()
ser.open()
if ser.is_open==True:
    print("\nAll right, serial port now open. Configuration:\n")
    print(ser, "\n") #print serial parameters

# Create figure for plotting
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
xs = [] #store trials here (n)
ys = [] #store relative frequency here
rs = []

max_readings_num = 100

cnt = 0
scale = 20.9
offset = 108300

import re
reg = r'^.*\s+raw:\s+(-?\d+(\.\d+)?).*$'

# This function is called periodically from FuncAnimation
def animate(i, xs, ys):
    global cnt

    #Aquire and parse data from serial port
    line=ser.readline()      #ascii
    try:
        line = line.decode('utf8').strip()
    except:
        return
    matchRes = re.match(reg, line)
    if not matchRes:
        print("failed: " + line)
        return

    value = float(matchRes.group(1))
    print(line)

    # Add x and y to lists
    xs.append(cnt)
    if len(xs) > max_readings_num:
        xs.pop(0)
    ys.append(value)
    if len(ys) > max_readings_num:
        ys.pop(0)
    cnt += 1

    # Draw x and y lists
    ax.clear()
    ax.plot(xs, ys, label="raw measurement")


# Set up plot to call animate() function periodically
ani = animation.FuncAnimation(fig, animate, fargs=(xs, ys), interval=10)
plt.xticks(rotation=45, ha='right')
plt.subplots_adjust(bottom=0.30)
plt.title('Raw weight monitoring...')
plt.ylabel('raw value')
plt.legend()
plt.show()
