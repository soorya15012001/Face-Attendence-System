import cv2
import numpy as np
import os

def facecrop(image): #returns the faces from the images
    facedata = "haarcascade_frontalface_alt.xml" #To find the faces in the images
    cascade = cv2.CascadeClassifier(facedata)

    img = cv2.imread(image)

    miniframe = cv2.resize(img, (250,250))

    faces = cascade.detectMultiScale(miniframe)

    for f in faces:
        x, y, w, h = [ v for v in f ]
        cv2.rectangle(img, (x,y), (x+w,y+h), (255,255,255))

        sub_face = img[y:y+h, x:x+w]
        return sub_face



for i in os.listdir("data//"):
	for j in os.listdir("data//"+i):
		p = "data//"+i+"//"+j

		try:
			img = cv2.imread(p)
			hi = cv2.resize(img,(250,250))
			print(p)
			cv2.imwrite(p,hi)	

		except:
			print("deleting image======>",p)
			os.remove(p)
	
		if (len(os.listdir("data//"+i)) == 0):
			print("deleting folder======> data//",i)
			os.rmdir("data//"+i)


