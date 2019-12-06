from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import (
    NumericProperty, ReferenceListProperty, ObjectProperty
)

class Test():
    def test(self):
        print("passssss click")


class OutlineApp(Widget):
    def __init__(self, **kwargs):
        super(OutlineApp, self).__init__(**kwargs)
        self.remove_widget(self.ids["btn_2_ID"])


    def test(self):
        self.ids["btn_1_ID"].text = "click"






class MyApp(App):
    def build(self):
        return OutlineApp()


MyApp().run()


