from kivy.uix.screenmanager import Screen
from panoptes_client import Panoptes


class LoginScreen(Screen):
    def login(self, *args):
        Panoptes.connect(
            username=self.ids['username'].text,
            password=self.ids['password'].text,
        )
        self.parent.current = 'projects'