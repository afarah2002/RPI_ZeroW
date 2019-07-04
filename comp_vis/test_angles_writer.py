#----------imports----------#
import numpy as np
import serial



#----------code starts here!----------#

#arduino
port = '/dev/ttyACM0'
ard = serial.Serial(port) 

angles = list(np.arange(0,180))
for i in angles:
	print(i)
	ard.write(str(i))
