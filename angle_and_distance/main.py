import cv2
import numpy as np
import dlib
from face_roi import Extract_eyes                       
from find_angle_distance import Find_angle_distance
from text import text

cap = cv2.VideoCapture(0)
eyes = Extract_eyes()

color = {
			"white":	(255, 255, 255),
			"red" : 	(0, 0, 255),
			"green" : 	(0, 255, 0),
			"blue" : 	(255, 0, 0),
			"yellow" : 	(0, 255, 255),
			"cyan" : 	(255, 255, 0),
			"magenta" : (255, 0, 255),
			"black" : 	(0, 0, 0)
			}

while True:
    
    _, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    eye = eyes.extract(gray)

    if eye:
        # Set Center Screen And Use Estimate Angle And Distance
        est_angle_distance = Find_angle_distance(eye["eye_center"], 5)
        vertical_view = est_angle_distance.estimate_angle_vertical()[0]
        horizotal_view = est_angle_distance.estimate_angle_horizontal()[0]
        distance_view = est_angle_distance.estimate_distance(eye["eye_right"])

        # Use Method Check Status Gaze View
        status_v_view = est_angle_distance.change_point_start_vertical()[1]
        status_h_view = est_angle_distance.change_point_start_horizontal()[1]

        # Print Value Of Angel And Distance
        list_print = [["Vertical view : ", vertical_view, "Horizotal view : ",
                        horizotal_view, "Distance view : ", distance_view]]

        for i in list_print:
            print("{}{:.2f}\N{DEGREE SIGN} {}{:.2f}\N{DEGREE SIGN} {}{:.2f} cm".\
                format(i[0], i[1], i[2], i[3], i[4], i[5]))

        # Draw Rectanngle And Text
        cv2.rectangle(frame, (eye["face"][0],eye["face"][1]), 
        					(eye["face"][2], eye["face"][3]), color["white"], 1)

        text_list = [   ["({}) {:.2f}\N{DEGREE SIGN}".format(status_v_view, 
                            vertical_view ), 15, color["red"]],
                        ["({}) {:.2f}\N{DEGREE SIGN}".format(status_h_view, 
                            horizotal_view ), 15, color["red"]],
                        ["{:.2f} (cm)".format(distance_view), 15, color["red"]]]       

        y = 26
        x = 5    
                     
        for i_text in text_list:
        	frame = text(frame, (x+eye["face"][0], abs(y-eye["face"][3])), 
        				                        i_text[0], i_text[1], i_text[2])
        	y += 22

    else:
    	print('No face')
    	frame = text(frame, (15,10), "Can't detect face !", 20, color["black"])

    cv2.imshow('out', frame)

    if cv2.waitKey(1) == 27 or cv2.getWindowProperty('out', 1) == -1:
        break

cap.release()
cv2.destroyAllWindows()

