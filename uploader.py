from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

from login_screen import LoginScreen
from projects_screen import ProjectsScreen


class UploaderApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(LoginScreen(name='login'))
        sm.add_widget(ProjectsScreen(name='projects'))
        return sm

if __name__ == '__main__':
    UploaderApp().run()