from kivy.app import App
from kivy.uix.image import Image
from kivy.clock import Clock
from kivy.graphics.texture import Texture
import cv2
import time
from kivy.uix.button import Button
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.config import Config
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from queue import Queue

q = Queue()

Builder.load_string('''
<MainScreen>:
    name: 'main'
    the_time: _id_lbl_time
    BoxLayout:
        orientation: 'vertical'
        Label:
            id: _id_lbl_time
            text: 'Time' 
            font_size: 60
 ''')



class Cap(Image):
    def __init__(self, **kwargs):
        super(Cap, self).__init__(**kwargs)
        self.orientation = "vertical"

        self.command = False
        self.cap = cv2.VideoCapture(0)
        Clock.schedule_interval(self.update, 1 / 30)

    def update(self, dt):

        _, self.frame = self.cap.read() # << This is frame!

        if self.command == True:
            cv2.circle(self.frame,(320,240), 50,2)

        buf1 = cv2.flip(self.frame, 0)
        buf = buf1.tostring()
        image_texture = Texture.create(size=(self.frame.shape[1], self.frame.shape[0]),
                                       colorfmt='bgr')
        image_texture.blit_buffer(buf, colorfmt='bgr', bufferfmt='ubyte')
        self.texture = image_texture

    def command_func1(self,obj):
        self.command = True

    def command_func2(self,obj):
        self.command = False

    def re_send(self, dt):
        return self.command


class MainScreen(Screen):
    pass
    def __init__(self,in_side, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
        Clock.schedule_interval(self.update_time, 1)
        self.in_side = in_side

    def update_time(self, dt):
        # MyTime = time.strftime("%H:%M:%S")
        self.the_time.text = self.in_side


class Btn(ToggleButton):
    def __init__(self, commad1, commad2, **kwargs):
        super(Btn, self).__init__(**kwargs)
        self.text = "CLICK"
        self.height = 50
        self.size_hint_y = None
        self.commad1 = commad1
        self.commad2 = commad2


    def on_state(self, widget, value):
        if value == 'down':
            self.text = "PLAY"
            self.commad1


        else:
            self.text = "START"
            self.commad2


class LayoutApp_app(BoxLayout):
    def __init__(self, **kwargs):
        super(LayoutApp_app, self).__init__(**kwargs)


        self.cap = Cap()

        self.orientation="vertical"


        self.box1 = BoxLayout(orientation="vertical")
        self.box2 = BoxLayout(orientation="vertical", height = 50, size_hint_y = None)
        self.box3 = BoxLayout(orientation="vertical", height = 50, size_hint_y = None)
        self.box3_2 = BoxLayout(orientation="horizontal")

        self.add_widget(self.box1)
        self.add_widget(self.box2)
        self.add_widget(self.box3)

        self.btn1 = Button(text="play",height = 50, size_hint_y = None)
        self.btn1.bind(on_press=self.cap.command_func1)
        self.btn2 = Button(text="camera",height = 50, size_hint_y = None)
        self.btn2.bind(on_press=self.cap.command_func2)

        self.box1.add_widget(self.cap)





        self.box3_2.add_widget(self.btn1)
        self.box3_2.add_widget(self.btn2)
        self.box3.add_widget(self.box3_2)















class BuildApp(App):
    def build(self):
        Window.size = (480,600)

        return Cap()



if __name__ == '__main__':
    BuildApp().run()