# pointer.py

from kivy.core.window import Window
from kivy.clock import Clock
from kivy.app import App

class HoverBehavior:
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Clock.schedule_interval(self.check_hover_loop, 0)
        self.mouse_is_over = False  # Tracker

    # hover logic
    def check_hover_loop(self, _dt):
        if not self.get_root_window():
            return  # wait for widgets
        if self.is_mouse_hovering_here():
            if not self.mouse_is_over:
                self.on_mouse_enter()
        else:
            if self.mouse_is_over:
                self.on_mouse_exit()
    
    # check if mouse is in widget change to pointer and update tracker
    def is_mouse_hovering_here(self):
        mouse_pos = Window.mouse_pos
        local_pos = self.to_widget(*mouse_pos)
        return self.collide_point(*local_pos)
    
    def on_mouse_enter(self):
        Window.set_system_cursor('hand')
        self.mouse_is_over = True

    def on_mouse_exit(self):
        self.mouse_is_over = False
    # reset if not in a button
        if not self.is_mouse_hovering_anywhere_else():
            Window.set_system_cursor('arrow')

    def is_mouse_hovering_anywhere_else(self):
        root = App.get_running_app().root

        for widget in root.walk():
            if widget is self:
                continue

            if isinstance(widget, HoverBehavior): #only check the ones that use hover behavior
                try:
                    local_mouse = widget.to_widget(*Window.mouse_pos)
                    if widget.collide_point(*local_mouse):
                        return True
                except:
                    pass

        return False
   