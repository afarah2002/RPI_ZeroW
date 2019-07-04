import cv2
import time
from matplotlib import pyplot as plt
import numpy as np
from copy import deepcopy
import random
from matplotlib.lines import Line2D
import matplotlib.pyplot as plt


#Arduino imports
import serial
port = '/dev/ttyACM0'
# arduino setup
ard = serial.Serial(port) 

def feed_process(feed):
	cap = cv2.VideoCapture(feed)
	print cap.isOpened()
	while cap.isOpened():
		ret, frame = cap.read()
		bin_thresh_low = 10
		bin_thresh_high = 25
		# k_dim = 20
		# kernel = np.ones((k_dim,k_dim),np.uint8)
		# thresh1 = cv2.erode(frame, kernel, iterations=2)

		# grayscale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		# ret, thresh1 = cv2.threshold(thresh1, bin_thresh_low,bin_thresh_high, cv2.THRESH_BINARY_INV) 
		hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
		k_dim = 2
		kernel = np.ones((k_dim,k_dim),np.uint8)
		hsv = cv2.dilate(hsv, kernel, iterations=1)


		lower_black = np.array([0,100,0])
		upper_black = np.array([100,150,100])

		mask = cv2.inRange(hsv, lower_black, upper_black)

		# thresh1 = cv2.adaptiveThreshold(grayscale, 150, cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,3)

		im2,contours,hierarchy = cv2.findContours(mask, 1, 2)
		if len(contours) > 1:
			max_contours = max(contours, key = lambda x: cv2.contourArea(x))

			rows,cols = mask.shape[:2]
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
			servo_angle = float(abs(im_angle - 90))
			ard.write(str(servo_angle))
			#drawing the line:
			# line_x_val1 = img_center_x-1000*vx
			# line_y_val1 = img_center_y-1000*-vy

			# line_x_val2 = img_center_x+1000*vx
			# line_y_val2 = img_center_y+1000*-vy

			# print(x,y,vx,vy)
			# cv2.line(mask, (line_x_val1,line_y_val1), (line_x_val2,line_y_val2), (255,255,255), 5)

			# time.sleep(.01)
			print("Servo angle:", servo_angle)

		# cv2.imshow('mask', mask)
		

		if cv2.waitKey(5) & 0xFF == ord('q'):
			break
	cap.release()
	cv2.destroyAllWindows()

feed_process('testfootage1.avi')

