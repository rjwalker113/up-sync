from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

class FileListItem(BoxLayout):
    def __init__(self, entry, root, **kwargs):
        super().__init__(orientation="horizontal", **kwargs)
        self.entry = entry
        self.root = root

        self.add_widget(Label(text=entry.network_path))
        self.add_widget(Button(text="Sync", on_release=self.sync))

    def sync(self, *args):
        self.root.app.sync_logic.sync_entry(self.entry)
        self.root.refresh()
