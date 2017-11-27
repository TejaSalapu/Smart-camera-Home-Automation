import numpy as np
import cv2

detector= cv2.CascadeClassifier('/home/pi/opencv-3.2.0/data/haarcascades/haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)
Id=raw_input('enter your id')
i=0;
while(True):
    ret, img = cap.read();
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = detector.detectMultiScale(gray, 1.3, 5);
    for (x,y,w,h) in faces:
        
        i=i+1;
        cv2.imwrite("faces/visitor."+Id+'.'+str(i)+".jpg",gray[y:y+h,x:x+w])
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        cv2.waitKey(100);
    cv2.imshow('frame',img);
    cv2.waitKey(1);
    if i>20:
        break
    
cap.release()
cv2.destroyAllWindows()
