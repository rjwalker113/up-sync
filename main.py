# main.py
from config.config import APP_VERSION_STR
version = f"v{APP_VERSION_STR}"

from kivy.config import Config
Config.set('input', 'mouse', 'mouse,disable_multitouch')
Config.set('graphics', 'height', '1024')
Config.set('graphics', 'width', '600')
Config.set('graphics', 'resizable', '1')

from kivy.core.text import LabelBase
from kivy.core.window import Window
from layout.utils import resource_path, cleanup
from kivy.clock import Clock

# Window.icon = resource_path('assets/images/AppIcon.ico')


from kivy.app import App
from kivy.lang import Builder
from app.state import SyncState
from app.store import EncryptedStore
from app.root import RootWidget

class SyncApp(App):
    def build(self):
        self.store = EncryptedStore("data/sync_state.enc")
        self.state = SyncState()

        # Load saved state if available
        saved = self.store.load()
        if saved:
            self.state.load_from_dict(saved)

        return Root(app=self)

    def on_stop(self):
        # Save state on exit
        self.store.save(self.state.to_dict())

if __name__ == "__main__":
    SyncApp().run()