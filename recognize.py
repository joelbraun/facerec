from imutils.video import VideoStream
from imutils.video import FPS
import argparse
import imutils
import pickle
import time
import cv2

vs = VideoStream(src=0).start()
time.sleep(2.0)

fps = FPS().start()

faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

while True:
    frame = vs.read()
    frame = imutils.resize(frame, width=500)
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    rects = faceCascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30,30))
    
    if (not rects):
        print("not detected")

    for (x,y,w,h) in rects:
        print("detected")

        # # Create a window showing the identified face
        # cv2.rectangle(frame,(x,y),(x+w,y+h),(255,255,0),2)
        # cv2.namedWindow('me', cv2.WINDOW_NORMAL)
        # cv2.imshow('me', frame)
        # k=cv2.waitKey(0) # wait until key is returned