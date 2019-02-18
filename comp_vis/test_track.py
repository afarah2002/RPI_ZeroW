import cv2
import time
from matplotlib import pyplot as plt
import numpy as np
from copy import deepcopy
import random
from matplotlib.lines import Line2D
import matplotlib.pyplot as plt

def feed_process(feed):
	cap = cv2.VideoCapture(feed)
	print cap.isOpened()
	while cap.isOpened():
		ret, frame = cap.read()

		grayscale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		ret, thresh1 = cv2.threshold(grayscale, 65,255, cv2.THRESH_BINARY) 
		k_dim = 5
		kernel = np.ones((k_dim,k_dim),np.uint8)
		erode = cv2.erode(frame, kernel, iterations=3)
		ret, erode = cv2.threshold(erode, 0,255, cv2.THRESH_BINARY)
		m,b = calculate_regression(np.argwhere(erode))
		_ = find_inliers(m,b, erode.shape[:2])
		x1,y1,x2,y2 = _
		# print(_)
		print(m,b)
		cv2.line(thresh1, (x1,y1),(x2,y2),(0,0,0),4)
		cv2.line(thresh1, (erode.shape[0]/2,0),(erode.shape[0]/2,erode.shape[1]),(0,0,0),4)

		cv2.imshow('erode', thresh1)
		

		if cv2.waitKey(5) & 0xFF == ord('q'):
			break
	cap.release()
	cv2.destroyAllWindows()

def calculate_regression(points):
	points_new = points
	xs = points_new[:,0]
	ys = points_new[:,1]
	x_mean = np.mean(xs)
	y_mean = np.mean(ys)
	xy_mean = np.mean(np.multiply(xs,ys))
	x_squared_mean = np.mean(np.square(xs))
	m = ((np.multiply(x_mean,y_mean))-xy_mean)/((x_mean**2)-x_squared_mean)
	b = y_mean - (m*x_mean) #TODO
	return m,b

def find_inliers(m, b, shape):
	x,y = shape
	rng = list(range(0,x))
	bott = []
	top = []
	for i in range(0,x):
		yy = (m * i) + b
		if yy > 0:
			bott.append(i)
		else:
			break
	for i in rng[::-1]:
		yy = (m * i) + b
		if yy > 0:
			top.append(i)
		else:
			break
	x1 = min(bott)
	x2 = max(top)
	# print(x1,x2)
	x1, y1, x2, y2 = (x1, int(m*x1+b), x2, int(m*x2+b))
	return x1,y1,x2,y2

feed_process('testfootage1.avi')

