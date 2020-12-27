import cv2
import numpy as np
from keras.models import load_model

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

#image paths
img1_path = 'data/zico/Zico_0001.jpg' #Input image-1
img2_path = 'data/zico/Zico_0002.jpg' #Input image-2

#image arrays
a = facecrop(img1_path)
a = cv2.resize(a,(250,250))
img_a = a.reshape(1,250,250,3)

b = facecrop(img2_path)
b = cv2.resize(b,(250,250))
img_b = b.reshape(1,250,250,3)

#class prediction using our trained model
model = load_model('model3.h5') # model loading
pred = model.predict({'image1': img_a, 'image2': img_b})
if pred < 0.5:
	class_ = 'No'
else:
	class_ = 'Yes'

print("Image similarity metric as per our trained model: ", pred[0][0])
print("Prediction - Are both images of the same person?", class_)