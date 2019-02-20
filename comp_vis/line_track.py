import cv2
import numpy as np
import socket
import cPickle 
from copy import deepcopy
import zmq

#this is the line following code for the AVE

# context = zmq.Context()
# footage_socket = context.socket(zmq.PUB)
# footage_socket.connect('tcp://localhost:8082')

def detectLine(feed):#detects contrasting lines in feed
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
		print(np.arctan(m)*180/np.pi)
		

		if cv2.waitKey(5) & 0xFF == ord('q'):
			break
	cap.release()
	cv2.destroyAllWindows()
		

detectLine('http://192.168.1.180:8081/')
# detectLine('testfootage1.mp4')