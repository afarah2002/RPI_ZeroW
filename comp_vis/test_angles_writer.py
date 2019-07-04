#----------imports----------#
import numpy as np
import serial
import time


#----------code starts here!----------#

#arduino
port = '/dev/ttyACM0'
ard = serial.Serial(port) 

angles = list(np.arange(0,180))
for i in angles:
	time.sleep(.1)
	print(i)
	ard.write(str(i))
