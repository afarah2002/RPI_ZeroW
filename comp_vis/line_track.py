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
		# frame = np.float32(frame)
		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

		grayscale = cv2.imread('frame', cv2.IMREAD_GRAYSCALE)
		ret, thresh1 = cv2.threshold(grayscale, 0,100, cv2.THRESH_BINARY) 

		k_dim = 2
		kernel = np.ones((k_dim,k_dim))/(k_dim^2)
		erode = cv2.erode(thresh1, kernel, iterations=1)

		cv2.imshow('thresh1',gray)

		if cv2.waitKey(5) & 0xFF == ord('q'):
			break
	cap.release()
	cv2.destroyAllWindows()
		

detectLine('http://192.168.1.180:8081/')
# detectLine('testfootage1.mp4')