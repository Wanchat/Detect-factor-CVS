
from kivy.uix.behaviors.compoundselection import CompoundSelectionBehavior
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.behaviors import FocusBehavior
from kivy.core.window import Window
from kivy.app import App
from kivy.uix.label import Label
import time


class SelectableGrid(FocusBehavior, CompoundSelectionBehavior, GridLayout):

    def keyboard_on_key_down(self, window, keycode, text, modifiers):
        """Based on FocusBehavior that provides automatic keyboard
        access, key presses will be used to select children.
        """
        if super(SelectableGrid, self).keyboard_on_key_down(
            window, keycode, text, modifiers):
            return True
        if self.select_with_key_down(window, keycode, text, modifiers):
            return True
        return False

    def keyboard_on_key_up(self, window, keycode):
        """Based on FocusBehavior that provides automatic keyboard
        access, key release will be used to select children.
        """
        if super(SelectableGrid, self).keyboard_on_key_up(window, keycode):
            return True
        if self.select_with_key_up(window, keycode):
            return True
        return False

    def add_widget(self, widget):
        """ Override the adding of widgets so we can bind and catch their
        *on_touch_down* events. """
        widget.bind(on_touch_down=self.button_touch_down,
                    on_touch_up=self.button_touch_up)
        return super(SelectableGrid, self).add_widget(widget)

    def button_touch_down(self, button, touch):
        """ Use collision detection to select buttons when the touch occurs
        within their area. """
        if button.collide_point(*touch.pos):
            self.select_with_touch(button, touch)

    def button_touch_up(self, button, touch):
        """ Use collision detection to de-select buttons when the touch
        occurs outside their area and *touch_multiselect* is not True. """
        if not (button.collide_point(*touch.pos) or
                self.touch_multiselect):
            self.deselect_node(button)

    def select_node(self, node):
        node.background_color = (0, 0, 0, 0)
        return super(SelectableGrid, self).select_node(node)

    def deselect_node(self, node):
        node.background_color = (0, 1, 0, 1)
        super(SelectableGrid, self).deselect_node(node)

    def v(self, v):
        self.v = v


    def on_selected_nodes(self, gird, nodes):
        # print(nodes)
        if nodes == []:
            print(time.time())
            self.v


class TestApp(App):
    def build(self):
        grid = SelectableGrid(cols=1, rows=1, touch_multiselect=True,
                              multiselect=True)
        grid.v(self.test())

        self.b = Button(text="Button")

        # for i in range(0, 6):
        grid.add_widget(self.b)
        return grid

    def test(self):
        print("hello")


TestApp().run()