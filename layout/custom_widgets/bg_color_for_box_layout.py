from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Color, Rectangle
from kivy.properties import ListProperty


class BackgroundColorBoxLayout(BoxLayout):
    bg_color = ListProperty([1, 1, 1, 1]) 

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with self.canvas.before:
            self.bg_color_instruction = Color(*self.bg_color)
            self.bg_rect = Rectangle(pos = self.pos, size = self.size)

        self.bind(pos = self._update_bg, size = self._update_bg, bg_color = self._update_color)

    def _update_bg(self, *args):
        self.bg_rect.pos = self.pos
        self.bg_rect.size = self.size

    def _update_color(self, *args):
        self.bg_color_instruction.rgba = self.bg_color