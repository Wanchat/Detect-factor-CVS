from kivy.app import App
from kivy.uix.image import Image
from kivy.clock import Clock
from kivy.graphics.texture import Texture
import cv2
import time
from kivy.uix.button import Button
from kivy.lang import Builder
import time
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

class KivyCamera(Image):

    def __init__(self, capture, fps, **kwargs):
        super(KivyCamera, self).__init__(**kwargs)
        self.capture = capture

        self.t = 0
        self.fps_number = 0
        self.fps = 0

        Clock.schedule_interval(self.update, 1 / fps)


    def update(self, dt):
        t_start = time.time()
        ret, frame = self.capture.read()

        if self.fps < 30:
            self.fps_number = self.fps

        print(self.fps_number)

        # convert it to texture
        buf1 = cv2.flip(frame, 0)
        buf = buf1.tostring()
        image_texture = Texture.create(size=(frame.shape[1], frame.shape[0]), colorfmt='bgr')
        image_texture.blit_buffer(buf, colorfmt='bgr', bufferfmt='ubyte')
        # display image from the texture
        self.texture = image_texture
        self.fps = 1.0 / (time.time() - t_start)





class CamApp(App):
    def build(self):
        self.capture = cv2.VideoCapture(0)
        self.my_camera = KivyCamera(capture=self.capture, fps=30)
        return self.my_camera

    def on_stop(self):
        # without this, app will not exit even if the window is closed
        self.capture.release()


if __name__ == '__main__':
    CamApp().run()

