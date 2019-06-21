import cv2
import time
from matplotlib import pyplot as plt
import numpy as np
from copy import deepcopy
import random
from matplotlib.lines import Line2D
import matplotlib.pyplot as plt

def see_ball(feed):
	cap = cv2.VideoCapture(feed)
	print cap.isOpened()
	while cap.isOpened():
		ret, frame = cap.read()


		hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
		lower_blue = np.array([110,50,50]) 
		upper_blue = np.array([130,255,255])
	
		mask_blue = cv2.inRange(hsv, lower_blue, upper_blue)

		cv2.imshow('mask_red', mask_blue)
		

		if cv2.waitKey(5) & 0xFF == ord('q'):
			break
	cap.release()
	cv2.destroyAllWindows()	



video = raw_input("Which color?  ") + ".avi"
see_ball(video)