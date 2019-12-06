from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.properties import ObjectProperty

# class Test_gird(Widget):
#     l_app = ObjectProperty(None)
#
#     # self.add_widget(Label(text="hellollll"))
#     # pass
# class T(Test_gird, GridLayout):
#     def __init__(self, **kwargs):
#         super(T, self).__init__(**kwargs)
#         self.add_widget(Label(text="hellollll"))


class GridApp(GridLayout):
    def __init__(self, **kwargs):
        super(GridApp, self).__init__(**kwargs)

        self.cols = 3
        self.add_widget(Label(text="hellollll"))
        self.add_widget(Label(text="hellollll"))

class MyApp(App):
    def build(self):
        return GridApp()


if __name__ == '__main__':
    MyApp().run()