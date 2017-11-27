import cv2 
import numpy as np

def mainss():
    recognizer = cv2.face.createLBPHFaceRecognizer()
    recognizer.load('/home/pi/facedetection/recog/trainer.yml')
    cascadePath = "/home/pi/opencv-3.2.0/data/haarcascades/haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(cascadePath);
    a=1
    b=1
    k=1
    cam = cv2.VideoCapture(0)
    #font = cv2.cv.InitFont(cv2.cv.CV_FONT_HERSHEY_SIMPLEX, 1, 1, 0, 1, 1)
    while True:
        ret, im =cam.read()
        gray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
        faces=faceCascade.detectMultiScale(gray, 1.3,5)
        for(x,y,w,h) in faces:
            cv2.rectangle(im,(x,y),(x+w,y+h),(225,0,0),2)
            Id, conf = recognizer.predict(gray[y:y+h,x:x+w])
            print Id
            print conf
            if(conf<50):
                if(Id==1):
                    Id="teja"
                elif(Id==2):
                    Id="anusha"
                elif(Id==3):
                    Id="lee"
                elif(Id==4):
                    Id="sam"
                elif(Id==5):
                    Id="chinky"    
            else:
                Id="Unknown"
            Id1=Id
            if Id1!=Id:
                Id2=Id
                b=b+1
            else:
                a=a+1
            cv2.putText(im,str(Id), (x, y), cv2.FONT_HERSHEY_PLAIN, 1.5, (0, 255, 0), 2)    
           # cv2.cv.PutText(cv2.cv.fromarray(im),str(Id), (x,y+h),font, 255)
        cv2.imshow('im',im) 
        if cv2.waitKey(10) & 0xFF==ord('q'):
        #k=k+1
        #if k>8:
            break
    cam.release()
    cv2.destroyAllWindows()
    if a>b:
        return Id1
    else:
        return Id2
