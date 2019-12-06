import cv2
import time

cap = cv2.VideoCapture(1)

while True:
    s = time.time()
    _, frame = cap.read()
    cv2.imshow('out', frame)
    if cv2.waitKey(1) == 27:
        break

    # time.sleep(2)
    e = time.time()
    fps = 1.0/float(e-s)
    if fps < 100:
        print(fps)
    e = 0
    s = 0
    fps = 0

cv2.destroyAllWindows()
cap.release()
