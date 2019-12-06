from kivy.app import App
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.uix.image import Image
from kivy.clock import Clock
from kivy.graphics.texture import Texture
from kivy.properties import ObjectProperty, StringProperty
from kivy.lang.builder import Builder
from tensorflow.python.keras.preprocessing.image import img_to_array
from tensorflow.python.keras.models import load_model
import cv2
import time
import dlib
from imutils import face_utils
import numpy as np
from threading import Thread
from queue import Queue
# import notify2
from os import system
import platform


Builder.load_file("blinkKV.kv")

Window.size = (400,600)

queue_blink = Queue()

class ROIface:
    def __init__(self, model_face):

        # dlib function call model
        self.detector = dlib.get_frontal_face_detector()
        self.predictor = dlib.shape_predictor(model_face)
        self.marginW = 20
        self.marginH = 20
        self.rightEye = None
        self.leftEye = None

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

    def boxEYE(self, i): # << define shape eye
        p1 = i[0,0] - self.marginW, i[1,1] - self.marginH
        p2 = i[3,0] + self.marginW, i[4,1] + self.marginH
        return p1, p2 # << return point rectangle roi


class PD():
    def __init__(self, modelCNN, modelFACE):
        self.roi = ROIface(modelFACE) # << class ROIface
        self.m = load_model(modelCNN)
        self.PR = None
        self.PL = None
        self.labelR = None
        self.labelL = None
        self.status = None
        self.new_roiR = None
        self.new_roiL = None

    def imtoNUMPY(self, roiR, roiL):
        self.new_roiR = cv2.resize(roiR, (28, 28))
        self.new_roiR = self.new_roiR.astype("float") / 255.0
        self.new_roiR = img_to_array(self.new_roiR)
        self.new_roiR = np.expand_dims(self.new_roiR, axis=0)

        self.new_roiL = cv2.resize(roiL, (28, 28))
        self.new_roiL = self.new_roiL.astype("float") / 255.0
        self.new_roiL = img_to_array(self.new_roiL)
        self.new_roiL = np.expand_dims(self.new_roiL, axis=0)
        return self.new_roiR, self.new_roiL

    def pdict(self):
        self.PR = self.m.predict(self.new_roiR,)
        self.PL = self.m.predict(self.new_roiL)
        return self.PR[-1], self.PL[-1]

    def changeSCORE(self):
        R = self.PR[-1]
        L = self.PL[-1]

        if R[0] > R[1]:
            self.labelR = "closed"
        elif R[1] > R[0]:
            self.labelR = "opened"
        else:
            self.labelR = ""

        if L[0] > L[1]:
            self.labelL = "closed"
        elif L[1] > L[0]:
            self.labelL = "opened"
        else:
            self.labelL = ""

        return self.labelR, self.labelL

    def statusEYE(self):
        if self.labelR and self.labelL == "opened":
            self.status = "opened"
        elif self.labelR and self.labelL == "closed":
            self.status = "closed"
        else:
            self.status = "half"
        return self.status


    def resuiltBLINK(self, gray, im):
        r, l = self.roi.face_shape(gray) # << shape face from dlib
        rROI = self.roi.roiEYE(r,gray) # << find roi eye right
        lROI = self.roi.roiEYE(l,gray) # << find roi eye left

        f = [r,l] # << draws box of eyes
        for i in f:
            p1,p2 = self.roi.boxEYE(i)
            cv2.rectangle(im, p1, p2, (204,153,0), 2)

        self.imtoNUMPY(rROI, lROI) # << reshape image to numpy
        self.pdict() # << predict eyes
        self.changeSCORE() # << change score predict to closed and opened
        blinkSTATUS = self.statusEYE() # << status eye
        return blinkSTATUS

# Thread method
class Noti():
        
    def pop(self,title, message):

        if platform.system() == "Linux":
            path_icon = "~/.icons/Arrongin-icon-theme/status/symbolic/dialog-warning-symbolic.svg"
            notify2.init('app name')
            n = notify2.Notification(title, message, path_icon)
            n.show()
            time.sleep(3)
            n.close()
            exit()

        elif platform.system() == "Windows":
            system("pip install ....")

        elif platform.system() =="Darwin":
            system("pip install ....")
            
        else:
            pass


    def notific(self):
        item = queue_blink.get()
        title = f'YOUR HAVE {item} BLINKS/S'
        message = "The risk of computer vision syndrome"
        self.pop(title, message)
        # pop = system('notify-send "'+title+'" "'+message+'"')

    # Start thread method
    def start_notifi(self,nblink):
        queue_blink.put(nblink)
        notifi = Thread(target=self.notific)
        notifi.start()

class CameraCV(Image):
    def __init__(self, capture, fps, **kwargs):
        super(CameraCV, self).__init__(**kwargs)
        Clock.schedule_interval(self.update, 1 / fps)

        mCNN = "res/net2_gay_test_TF.h5"
        mFACE = "../res/shape_predictor_68_face_landmarks.dat"

        self.p = PD(mCNN, mFACE)
        # self.roi = ROIface(mFACE)
        self.noti = Noti()
        self.capture = capture
        self.t = 0
        self.fps_number = 0
        self.fps = 0
        self.command = False
        self.COUNTER = 0
        self.TOTAL = 0
        self.timeOPEN = 0
        self.timeNOFACE = 0
        self.minBLINK = 20
        self.sec = 10
        self.frame_status = 1
        self.numFRAME = 0


    def update(self, dt):
        t_start = time.time()
        ret, frame = self.capture.read() # <<< start frame app
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # open detect blink <<<
        if self.command == True:
            try:
                time_start = time.time() # << start time on app
                blinkSTATUS = self.p.resuiltBLINK(gray, frame)

                # counter number blink
                if blinkSTATUS == "closed":
                    self.COUNTER += 1
                else:
                    if self.COUNTER > self.frame_status:
                        self.TOTAL += 1
                    self.COUNTER = 0

                endTime = time.time() - time_start
                self.timeOPEN += endTime # << time of open detect 

                # notific risk
                if self.timeOPEN > self.sec:
                    if self.TOTAL < self.minBLINK:
                        print("-"*50)
                        self.noti.start_notifi(self.TOTAL)

                    # reset 1 sec.
                    self.timeOPEN = 0
                    self.TOTAL = 0

                print(f"blinks:{self.TOTAL} | frame: {self.COUNTER}")

                # self.timeNOFACE = 0 # << reset time finds face

            except:
                # time not finds face
                self.numFRAME += 1

            

            if self.numFRAME >34:
                print("reset.................")
                self.numFRAME = 0
                self.TOTAL = 0 # << reset time exit detect
                self.timeOPEN = 0

        else: # reset mathod <<<
            self.TOTAL = 0
            self.timeOPEN = 0

        if self.fps < 30:
            self.fps_number = self.fps

        # convert frame opencv to kivy
        cols = frame.shape[0]
        rows = frame.shape[1]
        buf1 = cv2.flip(frame, 0)
        buf = buf1.tostring()
        image_texture = Texture.create(size=(rows,cols), colorfmt='bgr')
        image_texture.blit_buffer(buf, colorfmt='bgr', bufferfmt='ubyte')
        self.texture = image_texture

        self.fps = 1.0 / (time.time() - t_start)


    def command_func1(self):
        self.command = True

    def command_func2(self):
        self.command = False

    def send_text(self, dt):
        if self.command == False:
            x = ""
            return x
        else:
            return f"Your are {self.TOTAL} blinks/sec."

class BlinkMain(Widget):

    def __init__(self, **kwargs):
        super(BlinkMain, self).__init__(**kwargs)
        Clock.schedule_interval(self.on_state, 1/30)

        self.lab = self.ids["lbID"]
        self.capture = cv2.VideoCapture(0)
        self.my_camera = CameraCV(capture=self.capture, fps=30)
        self.ids["camID"].add_widget(self.my_camera)

    def on_state(self, dt):
        texts = self.my_camera.send_text(dt)
        self.lab.text = texts

    def event_toggle(self):
        click = self.ids["btn_1_ID"].state == "down"
        toggle_btn=self.ids["btn_1_ID"]

        if click:
            self.my_camera.command_func1()
            toggle_btn.text = "Detecting Blink..."
        else:
            self.my_camera.command_func2()
            toggle_btn.text = "Start Detect"

class BlinkDetectionApp(App):
    def build(self):
        return BlinkMain()

if __name__ == '__main__':
    BlinkDetectionApp().run()