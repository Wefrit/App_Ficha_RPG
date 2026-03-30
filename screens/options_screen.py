from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.app import App

class  Options(Screen):
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
                            # Botão para a tela Stats
        stats_button = Button(
            text='Stats',
            size_hint_y=1,
        )
        stats_button.bind(on_press=self.go_to_stats)
                            # Botão para a tela Abilities/Attributes

        attributes_button = Button(
            text='Atributos',
            size_hint_y=1,
        )
        attributes_button.bind(on_press=self.go_to_attributes)
                            # Botão para voltar para Game Screen
        return_button = Button(
            text='Voltar',
            size_hint_y=1,
        )
        return_button.bind(on_press=self.go_to_game)
                    # Adicionar elementos ao option_layout
        option_layout.add_widget(Label(text='Opções',size_hint_y=2))
        option_layout.add_widget(Widget(size_hint_y=1))
        option_layout.add_widget(stats_button)
        option_layout.add_widget(attributes_button)
        option_layout.add_widget(return_button)
        option_layout.add_widget(Widget(size_hint_y=2))


                # Adicionar elementos ao main_layout
        main_layout.add_widget(Widget(size_hint_x=1))
        main_layout.add_widget(option_layout)
        main_layout.add_widget(Widget(size_hint_x=1))

                # Passar para screen
        self.add_widget(main_layout)

    def on_pre_enter(self):
        self.character = App.get_running_app().character
        
    def go_to_stats(self, instance):
        self.manager.current = "stats"

    def go_to_attributes(self,instance):
        self.manager.current = 'attributes'

    def go_to_game(self, instance):
        self.manager.current = 'game'
