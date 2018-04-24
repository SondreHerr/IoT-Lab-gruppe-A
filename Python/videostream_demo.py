# import the necessary packages
from imutils.video import VideoStream
import datetime
import argparse
import imutils
import time
import cv2
import numpy as np
import Person
 
# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-p", "--picamera", type=int, default=-1,
	help="whether or not the Raspberry Pi camera should be used")
args = vars(ap.parse_args())
 
# initialize the video stream and allow the cammera sensor to warmup
vs = VideoStream(usePiCamera=args["picamera"] > 0).start()
time.sleep(2.0)

#Create background substractor
fgbg = cv2.createBackgroundSubtractorMOG2(detectShadows = True)
kernelOp = np.ones((3,3),np.uint8)
kernelCl = np.ones((11,11),np.uint8)
#Variabler
font = cv2.FONT_HERSHEY_SIMPLEX
persons = []
max_p_age = 5
pid = 1
areaTH = 3000
# loop over the frames from the video stream
while True:
	# grab the frame from the threaded video stream and resize it
	# to have a maximum width of 400 pixels
	frame = vs.read()
	fgmask = fgbg.apply(frame) #Use the substractor 
	# draw the timestamp on the frame
	timestamp = datetime.datetime.now()
	ts = timestamp.strftime("%A %d %B %Y %I:%M:%S%p")
	cv2.putText(frame, ts, (10, frame.shape[0] - 10), cv2.FONT_HERSHEY_SIMPLEX,
		0.35, (0, 0, 255), 1)
 	
	ret,imBin= cv2.threshold(fgmask,200,255,cv2.THRESH_BINARY)
        #Opening (erode->dilate) para quitar ruido.
	mask = cv2.morphologyEx(imBin, cv2.MORPH_OPEN, kernelOp)
        #Closing (dilate -> erode) para juntar regiones blancas.
	mask =  cv2.morphologyEx(mask , cv2.MORPH_CLOSE, kernelCl)

	_, contours0, hierarchy = cv2.findContours(mask,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
	for cnt in contours0:
		cv2.drawContours(frame, cnt, -1, (0,255,0), 3, 8)
		area = cv2.contourArea(cnt)
	print(area)
	if area > areaTH:
		#################
		#   TRACKING    #
		#################
		M = cv2.moments(cnt)
		cx = int(M['m10']/M['m00'])
		cy = int(M['m01']/M['m00'])
		x,y,w,h = cv2.boundingRect(cnt)
		
		new = True
		for i in persons:
			if abs(x-i.getX()) <= w and abs(y-i.getY()) <= h:
				new = False
				i.updateCoords(cx,cy)
				break
		if new == True:
			p = Person.MyPerson(pid, cx, cy, max_p_age)
			persons.append(p)
			pid += 1

		cv2.circle(frame,(cx,cy), 5, (0,0,255), -1)
		img = cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
		cv2.drawContours(frame, cnt, -1, (0,255,0), 3)
	for i in persons:
		if len(i.getTracks()) >= 2:
			pts = np.array(i.getTracks(), np.int32)
			pts = pts.reshape((-1,1,2))
			frame = cv2.polylines(frame, [pts], False, i.getRGB())
		cv2.putText(frame, str(i.getId()), (i.getX(), i.getY()), font, 0.3, i.getRGB(), 1, cv2.LINE_AA)

	# show the frame
	cv2.imshow("Frame", frame)


	key = cv2.waitKey(1) & 0xFF
	# if the `q` key was pressed, break from the loop
	if key == ord("q"):
		break
 
# do a bit of cleanup
cv2.destroyAllWindows()
vs.stop()
