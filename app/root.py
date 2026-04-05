from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

from ui.filelist import FileList  # your per-entry widget

class RootWidget(BoxLayout):
    def __init__(self, app, **kwargs):
        super().__init__(orientation="vertical", **kwargs)
        self.app = app

        self.file_list = FileList(app)
        self.add_widget(self.file_list)

        controls = BoxLayout(size_hint_y=None, height="48dp")
        add_btn = Button(text="Add File")
        add_btn.bind(on_release=self.add_file)
        controls.add_widget(add_btn)

        self.add_widget(controls)
