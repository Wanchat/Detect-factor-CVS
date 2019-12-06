import cv2
import dlib
import numpy as np

path_im = r"data/face_2.jpg"
path_model = r"../res/shape_predictor_68.dat"
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(path_model)

def inde(shape, x1, y1):
	return shape.part(x1).x, shape.part(y1).y

def inde2(shape, idx1, idx2, axe):
	if axe == 0:
		point = abs(shape.part(idx1).x + int((shape.part(idx2).x - shape.part(idx1).x ) / 2))
	else:
		point = abs(shape.part(idx1).y + int((shape.part(idx2).y - shape.part(idx1).y ) / 2))
	return point

def find_both(p1, p2):
	if p1 > p2:
		p = p2 + int(abs(p1-p2)/2)
	else:
		p = p1 + int(abs(p1-p2)/2)
	return p

im = cv2.imread(path_im)

dets = detector(im, 1)

for k, d in enumerate(dets):
    print("Detection {}: Left: {} Top: {} Right: {} Bottom: {}".format(
        k, d.left(), d.top(), d.right(), d.bottom()))

    # Get the landmarks/parts for the face in box d.
    shape = predictor(im, d)

    c_2 = shape.part(39).x, shape.part(40).y
    c_1 = inde(shape, 36, 37)
    p1_x = inde2(shape, 36, 39, 0)

    p1_y = inde2(shape, 37, 41, 1)
    p2_x = inde2(shape, 42, 45, 0)
    p2_y = inde2(shape, 43, 47, 1)

    c_x = find_both(p1_x, p2_x)
    c_y = find_both(p1_y, p2_y)

    cv2.circle(im, (p1_x, p1_y), 2, (255,0,0), -1)
    cv2.circle(im, (p2_x, p2_y), 2, (255,0,0), -1)
    cv2.circle(im, (c_x, c_y), 2, (255,0,0), -1)

    cv2.rectangle(im, c_1, c_2, (0,255,0), 1)


    # for i in range(shape.num_parts): # Loop point on face.
    # 	center = shape.part(i).x, shape.part(i).y # Get x and y point to center.

    # 	c_1 = shape.part(36).x, shape.part(37).y
    # 	c_2 = shape.part(39).x, shape.part(40).y
    	
    # 	cv2.rectangle(im, c_1, c_2, (0,255,0), 1)
    # the list of (x, y)-coordinates
    # coords = np.zeros((shape.num_parts, 2), dtype="int")
    # for i in range(shape.num_parts):
    # 	coords[i] = (shape.part(i).x, shape.part(i).y)
    # print(coords[0])
	

cv2.imshow("out", im)
cv2.waitKey()