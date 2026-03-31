from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.app import App
from save_manager import save_character
from characters.characters import *
import os


class ClassSelectScreen(Screen):

    def __init__(self, **kw):
        super().__init__(**kw)

        main_layout = BoxLayout(
            orientation='vertical',
            spacing=5,
            padding=5,
        )

        self.name_input = TextInput(
            hint_text="Digite o nome do personagem",
            multiline=False,
            size_hint_y=0.2
        )

        main_layout.add_widget(self.name_input)

        upper_layout = BoxLayout(
            orientation='horizontal',
            spacing=10,
            padding=10,
            size_hint_y = 1
        )

        upper_classes = [Bardo, Gorgona, Fada, Golen, Vampiro]

        for classe in upper_classes:
            
            upper_class_box = Button(
                background_normal=classe.sprite,
                size_hint_x=1,
            )

            upper_class_box.bind(
                on_press=lambda instance, c=classe: self.select_class(c)
            )

            upper_layout.add_widget(upper_class_box)


        bottom_layout = BoxLayout(
            orientation='horizontal',
            spacing=10,
            padding=10,
            size_hint_y=1
        )

        bottom_classes = [Panda, Draconiano, Dríade, Elfo, Who]

        for classe in bottom_classes:
            bottom_class_box = Button(
                background_normal=classe.sprite,
                size_hint_x=1,
            )

            bottom_class_box.bind(
                on_press=lambda instance, c=classe: self.select_class(c)
            )

            bottom_layout.add_widget(bottom_class_box)

        main_layout.add_widget(upper_layout)
        main_layout.add_widget(bottom_layout)
        self.add_widget(main_layout)

    def select_class(self, classe):
        nome = self.name_input.text.strip()
        if not nome:
            nome = classe.default_name

        # Verifica se já existe um save com esse nome e classe
        filename = f"{classe.__name__}_{nome}.json"
        app = App.get_running_app()
        path = os.path.join(app.user_data_dir, filename)

        if os.path.exists(path):
            self.show_error(f"Já existe um {classe.__name__} chamado {nome}!")
            return

        personagem = classe(nome)
        App.get_running_app().character = personagem
        save_character(personagem)
        self.manager.current = "game"

    def show_error(self, message):
        from kivy.uix.popup import Popup
        from kivy.uix.label import Label
        popup = Popup(
            title='ERRO!',
            content=Label(text=message),
            size_hint=(0.6, 0.3)
        )
        popup.open()