import cv2
import numpy as np
import socket
import cPickle 
from copy import deepcopy

#this is the line following code for the AVE

def detectLine(feed):#detects contrasting lines in feed
	upper_thresh = 0
	lower_thresh = 10 #contrast thresholds

	k_dim = 5
	kernel = np.ones((k_dim,k_dim),np.uint8)

	cap = cv2.VideoCapture(feed) #access webcam feed from IPport#
	while (cap.isOpened()):
		ret, frame = cap.read()
		img = cv2.inRange(frame,lower_thresh,upper_thresh)
		img = cv2.morphologyEx(img,cv2.MORPH_CLOSE,kernel) #frame morphology for contrast
		print("processing")

		print("exporting image....")
		clientsocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		clientsocket.connect(('localhost',8082)) #connect to network
		data = cPickle.dumps(img)
		clientsocket.sendall(struct.pack("H", len(data))+data)

# def exportImage(img): #exports image to new port 
	
	# while True:
		

detectLine('http://192.168.1.180:8081/')