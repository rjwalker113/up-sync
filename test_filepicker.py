from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

from tkinter import Tk
from tkinter.filedialog import askopenfilename

from models.synclink import SyncLink

import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s:%(name)s:%(message)s"
)


class Root(BoxLayout):
    def open_picker(self, *args):
        Tk().withdraw()
        path = askopenfilename()
        if path:
            SyncLink(path)

class TestApp(App):
    def build(self):
        root = Root()
        plus_button = Button(
            text="+",
            font_size=64,
            size_hint=(None, None),
            size=(200, 200),
            on_release=root.open_picker
        )
        root.add_widget(plus_button)
        return root

if __name__ == "__main__":
    TestApp().run()
