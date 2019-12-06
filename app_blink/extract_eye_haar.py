import cv2

cap = cv2.VideoCapture(0)
face_haar = cv2.CascadeClassifier(r"../res/haarcascades/aarcascade_frontalface_default.xml")
eye_haar = cv2.CascadeClassifier(r"../res/haarcascades/aarcascade_eye.xml")

while True:
	_, frame = cap.read()
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	face = face_haar.detectMultiScale(gray, 1.1, 9)

	for x, y, w, h in face:
		cv2.rectangle(frame, (x,y), (x+w, y+h), (0,0,0), 2)
		roi_gray = gray[y:y+h, x:x+w]
		roi_color = frame[y:y+h, x:x+w]
		eyes = eye_haar.detectMultiScale(roi_gray, 1.1, 4)

		midle = x+(w/2)

		for f, (ex,ey,ew,eh) in enumerate(eyes):

			if f == 0:
				if x + ex > midle:
					cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,0,255),2) # left eye
				else:
					cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(255,0,0),2) # right eye
			elif f == 1:
				if x + ex > midle:
					cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,0,255),2) # left eye
				else:
					cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(255,0,0),2) # right eye
			else:
				pass

	cv2.imshow("OUT", frame)

	if cv2.waitKey(1) == 27:
		break

cap.release()
cv2.destroyAllWindows()
