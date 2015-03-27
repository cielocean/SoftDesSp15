""" Experiment with face detection and image filtering using OpenCV """

import cv2
import numpy as np
import random

cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier('/home/g/haarcascade_frontalface_alt.xml')
kernel = np.ones((21,21),'uint8')

while(True):
    # # Capture frame-by-frame
    # ret, frame = cap.read()

    # # Display the resulting frame
    # cv2.imshow('frame',frame)
    # if cv2.waitKey(1) & 0xFF == ord('q'):
    #     break

	ret, frame = cap.read()
	faces = face_cascade.detectMultiScale(frame, scaleFactor=1.2, minSize=(20,20))
	# for (x,y,w,h) in faces:
	#     cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255))

	#For blurring faces
	for (x,y,w,h) in faces:
		frame[y:y+h,x:x+w,:] = cv2.dilate(frame[y:y+h,x:x+w,:], kernel)
		# cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255))
		# cv2.circle(frame,(x+w/2,y+h/2),w/2,(0,100,200),-1)
		cv2.ellipse(frame,(x+w/2,y+h/2),(w/2,h*4/7),0,0,360,(0,100,200),-1)
		#Eyes
		rx = random.randint (-5,5)
		ry = random.randint (-3,3)
		rm = random.randint (3,8)
		eye = random.randint (0,1)

		cv2.ellipse(frame,(x+w/4,y+3*h/7),(w/8,w/8),0,200,340,(0,0,0),3)
		cv2.ellipse(frame,(x+3*w/4,y+3*h/7),(w/8,w/8),0,200,340,(0,0,0),3)
		
		# if eye ==0:
		# 	cv2.ellipse(frame,(x+w/4,y+2*h/6),(w/12,w/12),0,20,160,(0,0,0),3)
		# 	cv2.ellipse(frame,(x+3*w/4,y+2*h/6),(w/12,w/12),0,20,160,(0,0,0),3)
		

		cv2.circle(frame,(x+w/4-rx,y+4*h/7-ry),w/8,(180,180,220),-1)
		cv2.circle(frame,(x+3*w/4+rx,y+4*h/7+ry),w/8,(180,180,220),-1)
		#Mouth
		cv2.ellipse(frame,(x+w/2,y+2*h/3),(w/12,w/rm),0,5*rm,180-5*rm,(10,10,255),3)
		cv2.ellipse(frame,(x+w/2+w/12,y+2*h/3),(w/12,w/12),0,20,160,(10,10,255),3)
		cv2.ellipse(frame,(x+w/2-w/12,y+2*h/3),(w/12,w/12),0,20,160,(10,10,255),3)
		#Ears
		cv2.ellipse(frame,(x+w,y),(w/random.randint(6,8),w/random.randint(6,8)),0,180,450,(0,100,200),3)
		cv2.ellipse(frame,(x+w,y),(w/13,w/13),0,180,450,(255,255,255),3)
		cv2.ellipse(frame,(x,y),(w/random.randint(6,8),w/random.randint(6,8)),0,90,360,(0,100,200),3)
		cv2.ellipse(frame,(x,y),(w/13,w/13),0,90,360,(255,255,255),3)
		#Nose


	# Display the resulting frame
	cv2.imshow('frame',frame)
	if cv2.waitKey(1) & 0xFF == ord('q'):
	    break


# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()