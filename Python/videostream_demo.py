# import de nødvendige tillegg
from imutils.video import VideoStream
import datetime
import argparse
import imutils
import time
import cv2
import numpy as np
import Person
 
# konstrukter argument og parse argument
ap = argparse.ArgumentParser()
ap.add_argument("-p", "--picamera", type=int, default=-1,
	help="whether or not the Raspberry Pi camera should be used")
args = vars(ap.parse_args())
 
# Start video stream og la kamerasensor varme opp
vs = VideoStream(usePiCamera=args["picamera"] > 0).start()
time.sleep(2.0)

# Lage bakgrunn som kan trekkes fra video stream
fgbg = cv2.createBackgroundSubtractorMOG2(detectShadows = True)
kernelOp = np.ones((3,3),np.uint8)
kernelCl = np.ones((11,11),np.uint8)

#Variabler
font = cv2.FONT_HERSHEY_SIMPLEX
persons = []
max_p_age = 5
pid = 1
cnt_up = 0
cnt_down = 0
total = 0
h = 250
w = 330
areaTH = 3000
print('Area Threshold', areaTH)

#Definering og tegning av linjer
line_up = int(3*(h/10))
line_down   = int(6*(h/10))

up_limit =   int(1*(h/10))
down_limit = int(8*(h/10))

print("Red line y:",str(line_down))
print("Blue line y:", str(line_up))
line_down_color = (255,0,0)
line_up_color = (0,0,255)
pt1 =  [0, line_down];
pt2 =  [w, line_down];
pts_L1 = np.array([pt1,pt2], np.int32)
pts_L1 = pts_L1.reshape((-1,1,2))
pt3 =  [0, line_up];
pt4 =  [w, line_up];
pts_L2 = np.array([pt3,pt4], np.int32)
pts_L2 = pts_L2.reshape((-1,1,2))

pt5 =  [0, up_limit];
pt6 =  [w, up_limit];
pts_L3 = np.array([pt5,pt6], np.int32)
pts_L3 = pts_L3.reshape((-1,1,2))
pt7 =  [0, down_limit];
pt8 =  [w, down_limit];
pts_L4 = np.array([pt7,pt8], np.int32)
pts_L4 = pts_L4.reshape((-1,1,2))


# loop over the frames from the video stream
while True:
	# grab the frame from the threaded video stream and resize it
	# to have a maximum width of 400 pixels
	frame = vs.read()
	for i in persons:
		i.age_one()

	fgmask = fgbg.apply(frame)
	fgmask2 = fgbg.apply(frame)

 
	# draw the timestamp on the frame
	ret,imBin= cv2.threshold(fgmask,200,255,cv2.THRESH_BINARY)
	ret,imBin2= cv2.threshold(fgmask2,200,255,cv2.THRESH_BINARY)

        #Opening (erode->dilate) para quitar ruido.
	mask = cv2.morphologyEx(imBin, cv2.MORPH_OPEN, kernelOp)
	mask2 = cv2.morphologyEx(imBin2, cv2.MORPH_OPEN, kernelOp)

        #Closing (dilate -> erode) para juntar regiones blancas.
	mask =  cv2.morphologyEx(mask , cv2.MORPH_CLOSE, kernelCl)
	mask2 =  cv2.morphologyEx(mask2 , cv2.MORPH_CLOSE, kernelCl)


	_, contours0, hierarchy = cv2.findContours(mask,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
	for cnt in contours0:
		cv2.drawContours(frame, cnt, -1, (0,255,0), 3, 8)
		area = cv2.contourArea(cnt)

		if area > areaTH:
			#################
			#   TRACKING    #
			#################
			M = cv2.moments(cnt)
			cx = int(M['m10']/M['m00'])
			cy = int(M['m01']/M['m00'])
			x,y,w,h = cv2.boundingRect(cnt)
		
			new = True
			if cy in range(up_limit, down_limit):
				for i in persons:
					if abs(cx-i.getX()) <= w and abs(cy-i.getY()) <= h:
						new = False
						i.updateCoords(cx,cy)
						if i.going_UP(line_down,line_up) == True:
							cnt_up += 1
							print("ID:",i.getId(),'crossed going up at',time.strftime("%c"))
						elif i.going_DOWN(line_down,line_up) == True:
							cnt_down += 1
							print("ID:",i.getId(),'crossed going down at',time.strftime("%c"))
						break
					if i.getState() == '1':
						if i.getDir() == 'down' and i.getY() > down_limit:
							i.setDone()
						elif i.getDir() == 'up' and i.getY < up_limit:
							i.setDone()
					if i.timedOut():
						index = persons.index(i)
						persons.pop(index)
						del i
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
	str_up = 'UP: '+ str(cnt_up)
	str_down = 'DOWN: '+ str(cnt_down)
	if (cnt_up - cnt_down >= 0):
		total = cnt_up - cnt_down
	else:
		total = 0
	str_total = 'TOT: '+ str(total)
	frame = cv2.polylines(frame,[pts_L1],False,line_down_color,thickness=2)
	frame = cv2.polylines(frame,[pts_L2],False,line_up_color,thickness=2)
	frame = cv2.polylines(frame,[pts_L3],False,(255,255,255),thickness=1)
	frame = cv2.polylines(frame,[pts_L4],False,(255,255,255),thickness=1)
	cv2.putText(frame, str_up ,(10,40),font,0.5,(255,255,255),2,cv2.LINE_AA)
	cv2.putText(frame, str_up ,(10,40),font,0.5,(0,0,255),1,cv2.LINE_AA)
	cv2.putText(frame, str_down ,(10,90),font,0.5,(255,255,255),2,cv2.LINE_AA)
	cv2.putText(frame, str_down ,(10,90),font,0.5,(255,0,0),1,cv2.LINE_AA)
	cv2.putText(frame, str_total ,(10,140),font,0.5,(255,255,255),2,cv2.LINE_AA)
	cv2.putText(frame, str_total ,(10,140),font,0.5,(0,255,0),1,cv2.LINE_AA)


	
	# show the frame
	cv2.imshow("Frame", frame)


	key = cv2.waitKey(1) & 0xFF
	# if the `q` key was pressed, break from the loop
	if key == ord("q"):
		break
 
# do a bit of cleanup
cv2.destroyAllWindows()
vs.stop()
