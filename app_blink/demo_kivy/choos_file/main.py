from kivy.app import App
from kivy.uix.popup import Popup
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.properties import ObjectProperty, StringProperty
from kivy.lang import Builder


class FileChoosePopup(Popup):
    load = ObjectProperty()


class Tab(TabbedPanel):
    file_path = StringProperty("No file chosen")
    the_popup = ObjectProperty(None)

    def open_popup(self):
        self.the_popup = FileChoosePopup(load=self.load)
        self.the_popup.open()

    def load(self, selection):
        self.file_path = str(selection[0])
        self.the_popup.dismiss()
        print(self.file_path)

        # check for non-empty list i.e. file selected
        if self.file_path:
            self.ids.get_file.text = self.file_path


Builder.load_file('main.kv')


class TestApp(App):

    def build(self):
        return Tab()

if __name__ == "__main__":
    TestApp().run()