import cv2
import time
from matplotlib import pyplot as plt
import numpy as np
from copy import deepcopy
import random
from matplotlib.lines import Line2D
import matplotlib.pyplot as plt
import struct 

#Arduino imports
import serial
port = '/dev/ttyACM0'
# port = 'COM3'
#arduino setup
ard = serial.Serial(port, 9600,timeout=3.0) 
angles = [0]

def feed_process(feed):
	cap = cv2.VideoCapture(feed)
	print cap.isOpened()
	while cap.isOpened():
		ret, frame = cap.read()

		grayscale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		ret, thresh1 = cv2.threshold(grayscale, 65,255, cv2.THRESH_BINARY_INV) 
		k_dim = 10
		kernel = np.ones((k_dim,k_dim),np.uint8)
		thresh1 = cv2.erode(thresh1, kernel, iterations=4)

		im2,contours,hierarchy = cv2.findContours(thresh1, 1, 2)
		if len(contours) > 0:
			max_contours = max(contours, key = lambda x: cv2.contourArea(x))

			rows,cols = thresh1.shape[:2]
			img_center_x, img_center_y = rows/2, cols/2
			p_frame_center = (img_center_x,img_center_y)

			[vx,vy,x,y] = cv2.fitLine(max_contours, cv2.DIST_L2,0,0.01,0.01)
			
			# switch to proper coordinates

			x -= img_center_x
			y = -(y - img_center_y)
			
			
			vx = vx
			vy *= -1

			if vx == 0:
				vx = 0.01


			m = vy/vx
			b = y - m*x
			im_angle = np.arctan(1/m)*180/np.pi

		# print(im_angle)
		servo_angle = round(int(abs(im_angle[0] - 90)), -1)
		if servo_angle != angles[-1]:
			angles.append(servo_angle)
		binary = struct.pack('>B', angles[-1])
		ard.write(binary)
		# time.sleep(.25)
		# ard.write(angles[-1])
		print("Servo angle:", angles[-1],binary)
		# print(type(servo_angle))
		cv2.imshow('thresh1', thresh1)

		if cv2.waitKey(5) & 0xFF == ord('q'):
			break
	cap.release()
	cv2.destroyAllWindows()

# def send_angles(im_angle)

feed_process('testfootage1.avi')

