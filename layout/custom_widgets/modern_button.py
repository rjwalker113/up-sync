# layout/rounded_button.py
# Creates rounded button style with a background color

from kivy.uix.button import Button
from kivy.graphics import Color, RoundedRectangle
from layout.custom_widgets.pointer import HoverBehavior
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.app import App

class RoundedButton(Button):
    def __init__(self, **kwargs):
        bg_rgba = kwargs.pop('bg_rgba', (0.031, 0.447, 0.729, 1))  # default color so no errors here
        radius = kwargs.pop('radius', [10])
        super().__init__(**kwargs)

        self.background_normal = ''
        self.background_color = (0, 0, 0, 0)

        with self.canvas.before:
            self.bg_color = Color(rgba=bg_rgba) #set background color
            self.rect = RoundedRectangle(radius= radius)

        self.bind(pos=self.update_shape, size=self.update_shape)

    def update_shape(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size


class ModernButton(RoundedButton, HoverBehavior):
    pass
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.default_color = (0.015, 0.35, 0.6, 1)  # transparent by default
        self.hover_color = 	(0.0, 0.2, 0.4, 1)  # highlight color

        self.default_color = self.bg_color.rgba

        self._hovering = False

        Clock.schedule_interval(self._check_hover, 1 / 30.0)

    def _check_hover(self, dt):
        if not self.get_root_window():
            return

        pos = Window.mouse_pos
        local = self.to_widget(*pos)
        is_hovered = self.collide_point(*local)

        if is_hovered and not self._hovering:
            self._hovering = True
            self.bg_color.rgba = self.hover_color
            Window.set_system_cursor('hand')

        elif not is_hovered and self._hovering:
            self._hovering = False
            self.bg_color.rgba = self.default_color

            if not self._any_other_hovered():
                Window.set_system_cursor('arrow')

    def _any_other_hovered(self):
        root = App.get_running_app().root
        for widget in root.walk():
            if widget is self:
                continue
            if isinstance(widget, ModernButton):
                try:
                    if widget.collide_point(*widget.to_widget(*Window.mouse_pos)):
                        return True
                except:
                    pass
        return False

