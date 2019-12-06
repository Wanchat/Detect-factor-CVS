import dlib
import imutils
from imutils import face_utils
import cv2
from roi import Extract_eyes
# from keras.models import load_model
from keras_preprocessing.image import img_to_array
import numpy as np

class ROIface:
    def __init__(self, model_face):

        # dlib function call model
        self.detector = dlib.get_frontal_face_detector()
        self.predictor = dlib.shape_predictor(model_face)
        self.marginW = 5
        self.marginH = 5

    def face_shape(self,image_gray):

        self.detect_from_model = self.detector(image_gray, 0)

        if self.detect_from_model is not None:

            for i in self.detect_from_model:
                self.shape = self.predictor(image_gray, i)
                self.shape = face_utils.shape_to_np(self.shape)

                self.leftEye = self.shape[36:42]
                self.rightEye = self.shape[42:48]

                return self.rightEye, self.leftEye
        else:
            return False
            

    def roiEYE(self, Eye,im):
        self.im = im
        self.Eye = Eye

        y1 = self.Eye[1,1]
        y2 = self.Eye[4,1]
        x1 = self.Eye[0,0]
        x2 = self.Eye[3,0]

        return self.im[ y1 - self.marginH: y2 + self.marginH,
                        x1 - self.marginW: x2 + self.marginW]

    def boxEYE(self, Eye): # << define shape eye

        p1 = Eye[0,0] - self.marginW, Eye[1,1] - self.marginH
        p2 = Eye[3,0] + self.marginW, Eye[4,1] + self.marginH

        return p1, p2 # << return point rectangle roi
         
   
class Pridict():
        def __init__(self, model):
            self.net = cv2.dnn.readNet(model)

        def cvNET(self, im):
            self.net.setInput(cv2.dnn.blobFromImage(im,
                size=(28, 28),
                swapRB=True,
                crop=False))
            return self.net.forward()

        def statusBLINK(self, status):
            if status[0] > status[1]:
                blink = "closed"
            else:
                blink = "opened"
            return  blink

def imtoNUMPY(roi):
        new_roi = cv2.resize(roi, (28, 28))
        new_roi = new_roi.astype("float") / 255.0
        new_roi = img_to_array(new_roi)
        new_roi = np.expand_dims(new_roi, axis=0)
        return new_roi

if __name__ == '__main__':

    face_model = r"../res/shape_predictor_68_face_landmarks.dat"
    im = cv2.imread(r"train_model/data/face_2.jpg")
    path_modelCNN = r"train_model/model/lenet2G_500_TF.pb"
    path_modelKERAS = r"train_model/model/lenet2G_500_TF.pb"

    # roi = ROIface(face_model)
    p = Pridict(path_modelKERAS)
    # m = load_model(path_modelCNN)

    # extand_eyes = Extand_eyes(face_model)
    # blinkcnn = Blink_cnn()

    cap = cv2.VideoCapture(0)
    pre = []
    frame_num = 0

    while True:
        frame_num += 1
        _, frame = cap.read()

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # eye = eyes.extract(gray)
        # faceShape = roi.face_shape(gray)

        face = extand_eyes.extend(gray)

        rEye = face["rightEye"]
        lEye = face["leftEye"]

        r, l = blinkcnn.extend_eyes(frame, rEye, lEye)

        cv2.imwrite(f"new_color{frame_num}.jpg", r)

        if frame_num > 100:
            break

        cv2.imshow("out", frame)
        if cv2.waitKey(1) == 27:
            break
    np.savetxt("predic.csv", pre)
    cap.release()
    cv2.destroyAllWindows()


    

