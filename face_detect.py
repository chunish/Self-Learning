#coding=utf-8
import numpy as np
import cv2
import cv2.cv as cv
from matplotlib import pyplot as plt
face_cascade = cv2.CascadeClassifier('D:\\opencv\\sources\\data\\haarcascades\\haarcascade_frontalface_default.xml')
img = cv2.imread('C:\\Users\SHEN\\Pictures\\Camera Roll\\a.jpg')
gray = cv2.cvtColor(img,cv2.cv.CV_BGR2GRAY)
divisor=1
h, w =np.shape(img)[:2]
minSize=(w/divisor, h/divisor)
color = (0,0,0)
faces = face_cascade.detectMultiScale(gray, 1.2, 2, cv2.CASCADE_SCALE_IMAGE,minSize)
roi = gray
if len(faces)>0:
	for faceRect in faces:
		x, y, w, h = faceRect
		cv2.rectangle(img, (x, y), (x+w, y+h), color)
		roi = img[y:(h+y), x:(w+x)]
cv2.imshow('img',img)
cv2.imshow('facerect',roi)
cv2.waitKey(0)
cv2.destroyAllWindows()