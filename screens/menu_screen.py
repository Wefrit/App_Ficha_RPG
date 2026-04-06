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
        new_character_button.bind(on_press=self.open_class_popup)

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


    def get_all_classes(self):
        import inspect
        import characters.characters as chars

        classes = []

        for name, obj in inspect.getmembers(chars):
            if inspect.isclass(obj):
                if issubclass(obj, chars.Character) and obj is not chars.Character:
                    
                    # 🔥 GARANTE que só entra classe jogável
                    if hasattr(obj, "sprite"):
                        classes.append(obj)

        return classes

    def open_class_popup(self, instance):
        from kivy.uix.popup import Popup
        from kivy.uix.boxlayout import BoxLayout
        from kivy.uix.button import Button
        from kivy.uix.scrollview import ScrollView
        from kivy.uix.gridlayout import GridLayout

        # layout principal
        layout = BoxLayout(orientation='vertical', spacing=10, padding=10)

        # scroll (caso tenha muitas classes)
        scroll = ScrollView()

        # grid com 2 colunas
        grid = GridLayout(
            cols=2,
            spacing=10,
            size_hint_y=None
        )
        grid.bind(minimum_height=grid.setter('height'))

        # pegar classes automaticamente
        classes = self.get_all_classes()

        # criar botão pra cada classe
        for classe in classes:
            btn = Button(
                text=classe.__name__,
                size_hint_y=None,
                height=80
            )

            btn.bind(on_press=lambda inst, c=classe: self.open_name_popup(c, popup))

            grid.add_widget(btn)

        scroll.add_widget(grid)
        layout.add_widget(scroll)

        # botão cancelar
        cancel_btn = Button(text="Cancelar", size_hint_y=0.2)
        layout.add_widget(cancel_btn)

        popup = Popup(
            title="Selecionar Classe",
            content=layout,
            size_hint=(0.8, 0.8)
        )

        cancel_btn.bind(on_press=popup.dismiss)

        popup.open()

    def open_name_popup(self, classe, previous_popup):
        from kivy.uix.popup import Popup
        from kivy.uix.boxlayout import BoxLayout
        from kivy.uix.button import Button
        from kivy.uix.textinput import TextInput

        previous_popup.dismiss()

        layout = BoxLayout(orientation='vertical', spacing=10, padding=20)

        name_input = TextInput(
            hint_text="Nome do personagem",
            multiline=False,
            size_hint_y=0.4
        )

        buttons = BoxLayout(size_hint_y=0.3, spacing=10)

        back_btn = Button(text="Voltar")
        create_btn = Button(text="Criar")

        buttons.add_widget(back_btn)
        buttons.add_widget(create_btn)

        layout.add_widget(name_input)
        layout.add_widget(buttons)

        popup = Popup(
            title=f"Criar {classe.__name__}",
            content=layout,
            size_hint=(0.7, 0.5)
        )

        # botão voltar
        back_btn.bind(on_press=lambda inst: [popup.dismiss(), self.open_class_popup(None)])

        # botão criar 
        create_btn.bind(
            on_press=lambda inst: self.create_character(classe, name_input.text, popup)
        )

        popup.open()

    def create_character(self, classe, nome, popup):
        import os
        from kivy.app import App
        from save_manager import save_character

        nome = nome.strip()

        if not nome:
            nome = classe.default_name

        filename = f"{classe.__name__}_{nome}.json"
        app = App.get_running_app()
        path = os.path.join(app.user_data_dir, filename)

        # verifica se já existe
        if os.path.exists(path):
            self.show_error(f"Já existe um {classe.__name__} chamado {nome}!")
            return

        personagem = classe(nome)

        App.get_running_app().character = personagem
        save_character(personagem)

        popup.dismiss()
        self.manager.current = "game"

    def show_error(self, message):
        from kivy.uix.popup import Popup
        from kivy.uix.label import Label

        popup = Popup(
            title='Erro',
            content=Label(text=message),
            size_hint=(0.6, 0.3)
        )
        popup.open()