from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout

from ui.filelistitem import FileListItem

class FileList(ScrollView):
    def __init__(self, app, **kwargs):
        super().__init__(**kwargs)
        self.app = app

        self.layout = GridLayout(cols=1, size_hint_y=None, spacing=4)
        self.layout.bind(minimum_height=self.layout.setter("height"))
        self.add_widget(self.layout)

        self.refresh()

    def refresh(self):
        self.layout.clear_widgets()

        for entry in self.app.state.entries:
            item = FileListItem(entry, root=self)
            self.layout.add_widget(item)
