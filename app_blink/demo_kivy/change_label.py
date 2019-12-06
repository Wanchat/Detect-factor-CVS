from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty, StringProperty
from kivy.clock import Clock
import time
from datetime import datetime

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

class MainScreen(Screen):

    def update_time(self, sec):
        MyTime = time.strftime("%H:%M:%S")
        self.the_time.text = MyTime


class ScreenManagerApp(App):

    def build(self):
        self.main_screen = MainScreen()
        return self.main_screen

    def on_start(self):
        Clock.schedule_interval(self.main_screen.update_time, 1)

ScreenManagerApp().run()