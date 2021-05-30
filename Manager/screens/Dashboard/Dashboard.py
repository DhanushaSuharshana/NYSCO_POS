from kivy.lang import Builder
from kivymd.uix.screen import MDScreen
from kivy.animation import Animation

# KV
kv = '''
#:include screens/Dashboard/Dashboard.kv
'''

Builder.load_string(kv)


class DashboardScreen(MDScreen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.sidebar_hide = True

    def collapse_sidebar(self):
        if self.sidebar_hide:
            animate_sidebar = Animation(pos_hint={'center_x': 0}, duration=0.5)
            animate_sidebar.start(self.ids.sidebar)
            self.sidebar_hide = False
        else:
            animate_sidebar = Animation(pos_hint={'center_x': 1}, duration=0.5)
            animate_sidebar.start(self.ids.sidebar)
            self.sidebar_hide = True
