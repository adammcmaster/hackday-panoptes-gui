from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen
from panoptes_client import Panoptes, Project


class ProjectsScreen(Screen):
    def load_projects(self, *args):
        for project in Project.where(owner=Panoptes.client().username):
            self.children[0].add_widget(Button(text=project.title))