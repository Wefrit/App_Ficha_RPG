from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.app import App
from save_manager import list_saves, load_character
from kivy.uix.popup import Popup
import os
from kivy.app import App

class  MenuScreen(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.character = None
        
        # Layout principal
        main_layout = BoxLayout(
            orientation='horizontal',
        )

            # Dentro do layout
                # Box Opções
        option_layout = BoxLayout(
            orientation='vertical',
            size_hint_x=1,
            spacing=30,
            padding=20,
        )
                    # Dentro de Box Opções
                        # Botões
                            # Botão para continuar
        continue_button = Button(
            text='Continuar',
            size_hint_y=1,
        )
        continue_button.bind(on_press=self.go_to_load)
                            # Botão para a tela Class Selection

        new_character_button = Button(
            text='Novo Personagem',
            size_hint_y=1,
        )
        new_character_button.bind(on_press=self.go_to_class_selection)

                            # Botão para voltar para Fechar o jogo
        close_button = Button(
            text='Sair',
            size_hint_y=1,
        )
        close_button.bind(on_press=self.close_game)

                    # Adicionar elementos ao option_layout
        option_layout.add_widget(Label(text='Ficha RPG',size_hint_y=2))
        option_layout.add_widget(Widget(size_hint_y=1))
        option_layout.add_widget(continue_button)
        option_layout.add_widget(new_character_button)
        option_layout.add_widget(close_button)
        option_layout.add_widget(Widget(size_hint_y=2))

                # Adicionar elementos ao main_layout
        main_layout.add_widget(Widget(size_hint_x=1))
        main_layout.add_widget(option_layout)
        main_layout.add_widget(Widget(size_hint_x=1))

                # Passar para screen
        self.add_widget(main_layout)

    def load_selected(self, filename):
        character = load_character(filename)

        if character:
            character.normalize()
            App.get_running_app().character = character
            self.manager.current = "game"

    def go_to_class_selection(self,instance):       
        self.manager.current = 'class_select'

    def close_game(self, instance):
        App.get_running_app().stop()
 
    def go_to_load(self, instance):
        layout = BoxLayout(orientation='vertical', spacing=10, padding=20)

        saves = list_saves()

        popup = Popup(
            title='Carregar Personagem',
            content=layout,
            size_hint=(0.8, 0.8)
        )

        if not saves:
            layout.add_widget(Label(text="Nenhum save encontrado"))
        else:
            for save in saves:
                row = BoxLayout(orientation='horizontal', size_hint_y=None, height=40)

                # Botão carregar
                load_btn = Button(text=save)
                load_btn.bind(on_press=lambda btn, s=save: self.load_and_close(s, popup))

                # Botão apagar
                delete_btn = Button(text="X", size_hint_x=None, width=60)
                delete_btn.bind(on_press=lambda btn, s=save: self.delete_save_ui(s, layout, popup))

                row.add_widget(load_btn)
                row.add_widget(delete_btn)

                layout.add_widget(row)

        close_button = Button(text='Fechar', size_hint_y=0.2)
        close_button.bind(on_press=popup.dismiss)
        layout.add_widget(close_button)

        popup.open()

    def load_and_close(self, filename, popup):
        character = load_character(filename)

        if character:
            character.normalize()
            App.get_running_app().character = character
            popup.dismiss()
            self.manager.current = "game"

    def delete_save_ui(self, filename, layout, popup):
        app = App.get_running_app()
        path = os.path.join(app.user_data_dir, filename)

        if os.path.exists(path):
            os.remove(path)

        popup.dismiss()
        self.go_to_load(None)
