# layout/custom_popup.py
# Creates a popup with a title, message and OK button for showing outputs and errors where we want to terminate the app.

from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.clock import Clock
from kivy.metrics import dp
from kivy.app import App
from layout.custom_widgets.modern_button import ModernButton

class CustomPopup(Popup):
    def __init__(self, popup_title, popup_message, close_app=False, **kwargs):
        super().__init__(
            title=popup_title, 
            size_hint=(0.5, None),
            auto_dismiss=False, # Prevent closing if clicking outside of the popup
            **kwargs)

        self.close_app = close_app
        self.setup_ui(popup_message)

        # Schedule size adjustment after layout is visible
        Clock.schedule_once(self.adjust_sizes, 0)

    def setup_ui(self, message):
        self.message_label = Label(text=message, halign='center', valign='middle', size_hint_y=None)
        
        # Create container for all elements
        self.main_layout = BoxLayout(orientation='vertical', padding=[dp(10),dp(40),dp(10),dp(20)], spacing=dp(30), size_hint=(1, None))
        
        # Create and configure OK button
        self.ok_button = ModernButton(text="OK", size_hint=(None, None), size=(dp(100), dp(40)), pos_hint={"center_x": 0.5})
        self.ok_button.bind(on_press=self._on_button_press)
        
        # Add widgets to layout
        self.main_layout.add_widget(self.message_label)
        self.main_layout.add_widget(self.ok_button)
        
        # Set layout as popup content
        self.content = self.main_layout
        
    def adjust_sizes(self, *args):
        # Set text wrapping width to match layout width
        self.message_label.text_size = (self.main_layout.width, None)
        
        # Update label height based on wrapped text
        self.message_label.texture_update()
        label_height = self.message_label.texture_size[1]
        self.message_label.height = label_height
        
        # Calculate total popup height
        button_height = self.ok_button.height
        spacing = self.main_layout.spacing
        padding = self.main_layout.padding[1] * 2  # Top + bottom padding
        popup_title_height = 50  # ~ space for title bar
        
        total_height = (label_height + button_height + spacing + padding)
        
        self.main_layout.height = total_height
        self.height = total_height + popup_title_height

    def _on_button_press(self, instance):
        if self.close_app:
            App.get_running_app().stop()
        else:
            self.dismiss()