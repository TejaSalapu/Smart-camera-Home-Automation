To build a Physical home authentication system

"A camera and distance sensor are connected to a raspberry pi which gives the live video stream to the server which in turn transmits to android using socket programming.
-	How to read data from camera and distance sensor.

-How to detect faces using facial recognition program (opencv).

-How to send live video stream from Pi to server and display it on android.

-	Also gesture recognition as extra password for authentication."
EQUIPMENT : Raspberry pi Kit , distance sensor, USB camera module, speaker.

10 steps to build IOT system

1.	Install operating system for the raspberry pi using the following links. http://www.instructables.com/id/My-Raspberry-Pi-Setup/
2.	Connect a distance sensor to Raspberry Pi. You can use the Python library available at https://github.com/johnbryanmoore/VL53L0X_rasp_python to use the sensor.
 
 
3.	Install opencv software on Raspberry pi for Face Recognition. (Takes almost 4 hours :P ) https://www.pyimagesearch.com/2015/07/27/installing-opencv-3-0-for-both-python-2-7- and-python-3-on-your-raspberry-pi-2/

4.	Face Recognition

I.	face_detection.py - Firstly we capture images of users to feed the training data.
II.	Trainer.py - Train the algorithm with the image database of users
III.	Face_recognition.py - This program captures a image, detects the face and classifies the name of user.
 

5.	You may also implement Gesture recognition for authenticating the user along with face recognition
Gesture recognition

I.	Gesure.py - Detects the hand from webcam feed and identifies the unique gesture and checks that with password set by the owner.
 

6.	Now we need to set up server and obtain access keys for the server. You can set up ec2-server from here- https://aws.amazon.com/ec2/
7.	Install Android studio With sdk version 22
w.	need to run client server program on server and raspberry pi.
I.	Iot_final.py - this program runs on raspberry pi, it captures images of visitors of the house and gives the image input to facial recognition program which in turn
 
identifies the person's name. Then program verifies the user by checking in the database and sends stream of images to server.
II.	finalserver.py -This program runs on server which takes input image stream from the pi and gives the input to Android.
III.	Android app - It takes input from owner whether to authenticate the user or not and sends the authentication status to server which in turn sends it to pi.
9.	Now, when server sends authentication status to Pi it should give voice message "welcome home Teja!" , for this we need to install amazon TTS
10.	Install it from here- https://aws.amazon.com/polly/

