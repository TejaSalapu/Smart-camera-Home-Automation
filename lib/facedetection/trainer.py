import cv2,os
import numpy as np
from PIL import Image

recognizer = cv2.face.createLBPHFaceRecognizer()
detector= cv2.CascadeClassifier("/home/pi/opencv-3.2.0/data/haarcascades/haarcascade_frontalface_default.xml");

def getImagesAndLabels(path):
    imagePaths=[os.path.join(path,f) for f in os.listdir(path)] 
    faceSamples=[]
    Ids=[]
    for imagePath in imagePaths:
        pilImage=Image.open(imagePath).convert('L')
        imageNp=np.array(pilImage,'uint8')
        Id=int(os.path.split(imagePath)[-1].split(".")[1])
        faces=detector.detectMultiScale(imageNp)
        for (x,y,w,h) in faces:
            faceSamples.append(imageNp[y:y+h,x:x+w])
            Ids.append(Id)
    return faceSamples,np.array(Ids)
Ids,faces = getImagesAndLabels('/home/pi/face detection/faces')
recognizer.train(Ids, faces)
recognizer.save('recog/trainer.yml')
