from kivy.uix.screenmanager import ScreenManager
from kivymd.app import MDApp
from kivy.core.window import Window

from screens.SignIn.SignIn import SignInScreen
from screens.Dashboard.Dashboard import DashboardScreen

Window.size = (1024, 768)


class MyApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.title = "NYSCO"

    def build(self):
        sm = ScreenManager()
        sm.add_widget(SignInScreen(name='signIn'))
        sm.add_widget(DashboardScreen(name='dashboard'))
        sm.current = 'dashboard'

        return sm


MyApp().run()
