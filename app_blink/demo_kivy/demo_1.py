# from kivy.app import App
# from kivy.uix.label import Label
# from kivy.lang import Builder
# from kivy.properties import ObjectProperty
# from kivy.lang.builder import Builder
# from kivy.uix.widget import Widget
# from kivy.uix.gridlayout import GridLayout
# from kivy.uix.boxlayout import BoxLayout
# from kivy.uix.button import Button
#
#
# class Outline_App(BoxLayout):
#     def __init__(self, **kwargs):
#         super(Outline_App, self).__init__(**kwargs)
#         self.orientation="vertical"
#         self.add_widget(Button(text = 'Hello 1',size=(200, 50), size_hint=(None, None)))
#         self.add_widget(Button(text = 'Hello 1'))
#         self.add_widget(Button(text = 'Hello 1'))
#         self.add_widget(Button(text = 'Hello 1'))
#         self.row_force_default =False
#         self.row_default_height=50
#
#
#
#
# class MyApp(App):
#     def build(self):
#         return Outline_App()
#
# if __name__ == '__main__':
#     MyApp().run()


'''
Camera Example
==============

This example demonstrates a simple use of the camera. It shows a window with
a buttoned labelled 'play' to turn the camera on and off. Note that
not finding a camera, perhaps because gstreamer is not installed, will
throw an exception during the kv language processing.

'''

# Uncomment these lines to see all the messages
# from kivy.logger import Logger
# import logging
# Logger.setLevel(logging.TRACE)

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
import time
Builder.load_string('''
<CameraClick>:
    orientation: 'vertical'
    Camera:
        id: camera
        resolution: (640, 480)
        play: False
    ToggleButton:
        text: 'Play'
        on_press: camera.play = not camera.play
        on_press: test_p
        size_hint_y: None
        height: '48dp'
    Button:
        text: 'Capture'
        size_hint_y: None
        height: '48dp'
        on_press: root.capture()
''')


class CameraClick(BoxLayout):
    def capture(self):
        '''
        Function to capture the images and give them the names
        according to their captured time and date.
        '''
        camera = self.ids['camera']
        timestr = time.strftime("%Y%m%d_%H%M%S")
        camera.export_to_png("IMG_{}.png".format(timestr))
        print("Captured")

    def test_p(self):
        print("hello")


class TestCamera(App):

    def build(self):
        return CameraClick()


TestCamera().run()