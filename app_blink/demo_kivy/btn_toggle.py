# from kivy.uix.button import Button
# from kivy.app import App
# from functools import partial
#
# class KivyButton(App):
#
#     def disable(self, instance, *args):
#         instance.disabled = True
#
#     def update(self, instance, *args):
#         instance.text = "I am Disabled!"
#
#     def build(self):
#         mybtn = Button(text="Click me to disable")
#         mybtn.bind(on_press=partial(self.disable, mybtn))
#         mybtn.bind(on_press=partial(self.update, mybtn))
#
#         return mybtn
# KivyButton().run()


from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder

Builder.load_string("""
<BuildToggle>:
 
    ToggleButton:
        text: "CLICK 1"
        id: debug
        on_release: root.build()
""")

class BuildToggle(Widget):

    def build(self):
        debug = self.ids["debug"].state == "down"
        if debug:
            self.ids["debug"].text ="CLICK 2"
        else:
            self.ids["debug"].text ="CLICK 1"


class MyApp(App):

    def build(self):
        return BuildToggle()

MyApp().run()




























