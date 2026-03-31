from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from screens.game_screen import GameScreen
from screens.menu_screen import MenuScreen
from screens.class_select_screen import ClassSelectScreen
from screens.attributes_screen import AttributesScreen
from screens.options_screen import Options
from screens.stats_screen import Stats


class MainApp(App):
    def build(self):
        self.character = None
        sm = ScreenManager()

        sm.add_widget(MenuScreen(name='menu'))
        sm.add_widget(GameScreen(name="game"))
        sm.add_widget(ClassSelectScreen(name='class_select'))
        # sm.add_widget(AttributesScreen(name='attributes'))
        sm.add_widget(Options(name='options'))
        sm.add_widget(Stats(name='stats'))

        sm.current = 'menu'

        return sm


MainApp().run()
