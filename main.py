from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from screens.game_screen import GameScreen
from screens.menu_screen import MenuScreen
from screens.stats_screen import Stats


class MainApp(App):
    def build(self):
        self.character = None
        sm = ScreenManager()

        sm.add_widget(MenuScreen(name='menu'))
        sm.add_widget(GameScreen(name="game"))
        sm.add_widget(Stats(name='stats'))

        sm.current = 'menu'

        return sm


MainApp().run()
