 
import commands
import os
import sys

sys.path.insert(0,"/home/pi/pi-detector/scripts/")
from facematch import *
#sys.path.insert(1,"")
commands.getstatusoutput('fswebcam user.jpg')
sys.path.insert(0,"/home/pi/distance/VL53L0X_rasp_python/python/")
from VL53L0X_example import *
from tts_voice import *
sys.path.insert(0,"/home/pi/distance/VL53L0X_rasp_python/python/")
dist = mains()
sys.path.insert(0,"/home/pi/facedetection/")
from recogniser import *

img= 'user.jpg'

imgname=mainss()
from gesture import *
g=mainx()
if "1" in g:
    print "password accepted"
print dist
print img
print imgname
a=imgname+' '+str(dist)
print a
f=open("userinfo.txt","w")
f.write(a)
f.close()

#authenticate
with open('userinfo.txt','r') as f:
    line= f.readline()
    a=line.split()
with open('database.txt','r') as f:
    l=f.readline()
    b=l.split()
    if a[0] == b[0] and int(a[1]) >int(b[1]) and int(a[1])<int(b[2]):
        store=a[0]+' '+a[1]+' '+b[3]+' '+b[4]+' '+b[5]
with open('ex.txt','w') as f:
    f.write(store)


import socket                   # Import socket module

port = 65533                   # Reserve a port for your service.
s = socket.socket()             # Create a socket object
host = "ec2-18-220-130-139.us-east-2.compute.amazonaws.com"     # Get local machine name
                    # Now wait for client connection.
s.connect((host, port))
s.send("Hello server! ")

#while True:
filename='/home/pi/pi-detector/faces/faces.txt'
f = open("ex.txt",'rb')
l = f.read(500)
while (l):
    s.send(l)
    l = f.read(500)
f.close()
print('Done sending')
print('Successfully get the file')
s.close()

s = socket.socket()  
s.connect((host, port))
#s.send("Hello server! ")
data = 1
i = 1
while True:
    commands.getstatusoutput('fswebcam user.jpg')
    f = open("user.jpg",'rb')
    l = f.read()
    while (l):
        s.send(l)
        l = f.read()
    f.close()
    s.close()
    s = socket.socket() 
    s.connect((host, port))
    
    if i==5:
        break
    i=i + 1
    while True:
        data = s.recv(500)
        if ("1") in data:
            break
    data = 0
    


print('Done sending')
print('Successfully get the file')
#s.close()
#s = socket.socket()  
#s.connect((host, port))

print('connection alive')
datanot="0"
while True:
    with open('/home/pi/SampleFile.txt', 'wb') as f:
         print 'file opened'
         print('receiving data...')
         data = s.recv(500)
         print('data=%s', (data))
         if not data:
            f.write(datanot)
            break
        # write data to a file
         f.write(data)
    f.close()
    if data:        
        with open('/home/pi/SampleFile.txt','r') as f:
            n=f.readline()
            print n   
        if ("1") in n:
            open('/home/pi/SampleFile.txt','w').close()
            text= 'welcome home'+ imgname
            tts_amazon(text)
            break
        if ("0") in n:
            open('/home/pi/SampleFile.txt','w').close()
            text= 'system is unable to recognize you please try again'
            tts_amazon(text)
            break
