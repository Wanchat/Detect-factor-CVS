from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.uix.togglebutton import ToggleButton
from kivy.lang.builder import Builder
from kivy.uix.image import Image
from kivy.clock import Clock
from kivy.graphics.texture import Texture
import cv2
import time
from kivy.core.window import Window


Builder.load_file("my.kv")

class KivyCamera(Image):

    def __init__(self, capture, fps, **kwargs):
        super(KivyCamera, self).__init__(**kwargs)
        Clock.schedule_interval(self.update, 1 / fps)

        self.capture = capture
        self.t = 0
        self.fps_number = 0
        self.fps = 0


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

    def send_fps(self, dt):
        return self.fps_number


class OutlineApp(Widget):
    def __init__(self, **kwargs):
        super(OutlineApp, self).__init__(**kwargs)
        Clock.schedule_interval(self.on_state, 1 / 30)
        self.lab = self.ids["lbID"]

        self.capture = cv2.VideoCapture(0)
        self.my_camera = KivyCamera(capture=self.capture, fps=30)
        self.ids["camID"].add_widget(self.my_camera)

    def on_state(self, dt):
        texts = self.my_camera.send_fps(dt)
        # MyTime = time.strftime("%H:%M:%S")
        self.lab.text = str(texts)


class MytestappApp(App):

    def build(self):
        Window.size = (400, 600)
        return OutlineApp()

MytestappApp().run()