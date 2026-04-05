# custom_widgets\simple_popup.py
# Creates a simple modal popup with OK, and clicking OK executes a function.

from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

# class SimplePopup(Popup):
#     def __init__(self, message, on_ok_callback, **kwargs):
#         title = kwargs.pop("title", "Notice")  # Use provided title or default to "Notice"

#         super().__init__(
#             title=title,
#             size_hint=(None, None),
#             size=(400, 200),
#             auto_dismiss=False,
#             **kwargs
#         )

#         layout = BoxLayout(orientation='vertical', spacing=10, padding=20)

#         layout.add_widget(Label(text=message, halign='center', valign='middle'))

#         ok_button = Button(text="OK", size_hint=(1, None), height=40)
#         ok_button.bind(on_release=lambda *args: self._handle_ok(on_ok_callback))
#         layout.add_widget(ok_button)

#         self.content = layout

#     def _handle_ok(self, callback):
#         if callback:
#             callback()
#         self.dismiss()

# With loading button
from kivy.clock import Clock

class SimplePopup(Popup):
    def __init__(self, message, on_ok_callback, **kwargs):
        title = kwargs.pop("title", "Notice")
        super().__init__(
            title=title,
            size_hint=(None, None),
            size=(400, 200),
            auto_dismiss=False,
            **kwargs
        )

        layout = BoxLayout(orientation='vertical', spacing=10, padding=20)
        layout.add_widget(Label(text=message, halign='center', valign='middle'))

        self.ok_button = Button(text="OK", size_hint=(1, None), height=40)
        self.ok_button.bind(on_release=self._handle_ok)
        layout.add_widget(self.ok_button)

        self._callback = on_ok_callback
        self.content = layout

    def _handle_ok(self, *args):
        # Update button state immediately
        self.ok_button.text = "Loading"
        self.ok_button.disabled = True

        # Schedule the actual callback and dismissal on the next frame
        Clock.schedule_once(self._run_callback, 0)

    def _run_callback(self, dt):
        if self._callback:
            self._callback()
        self.dismiss()

