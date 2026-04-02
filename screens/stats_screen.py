from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from characters.characters import *
from kivy.app import App
from save_manager import save_character

class Stats(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.character = None
    
        # Main Layout
        main_layout = BoxLayout(
            orientation='horizontal',
        )
            # Elementos do main layout
                # Caixa de alterar stats
        change_stats_layout = BoxLayout(
            orientation='vertical',
            size_hint_x=1,
            spacing = 30,
            padding=30
        )
                    # Elementos da caixa de alterar stats
                        # Box de Hp
        hp_box_layout = BoxLayout(
            orientation='horizontal',
            size_hint_y=1,
        )
                            # Elementos da Box de Hp
        self.hp_label = Label(text='HP', size_hint_x=3)
        minus_hp_button = Button(text='-', size_hint_x=1)
        minus_hp_button.bind(on_press=self.minus_hp)
        plus_hp_button = Button(text='+', size_hint_x=1)
        plus_hp_button.bind(on_press=self.plus_hp)

                                # Adicionando os elementos À Caixa de HP
        hp_box_layout.add_widget(minus_hp_button)
        hp_box_layout.add_widget(self.hp_label) # Alterar para receber o valor do hp total
        hp_box_layout.add_widget(plus_hp_button)

                        # Box da Mana
        mana_box_layout = BoxLayout(
            orientation='horizontal',
            size_hint_y=1,
        )
                            # Elementos da Box de Mana
        self.mana_label = Label(text='Mana', size_hint_x=3)
        minus_mana_button = Button(text='-', size_hint_x=1)
        minus_mana_button.bind(on_press=self.minus_mana)

        plus_mana_button = Button(text='+', size_hint_x=1)
        plus_mana_button.bind(on_press=self.plus_mana)

                                # Adicionando os elementos À Caixa de Mana
        mana_box_layout.add_widget(minus_mana_button)
        mana_box_layout.add_widget(self.mana_label) # Alterar para receber o valor do mana total
        mana_box_layout.add_widget(plus_mana_button)

                        # Box da Deesa
        defense_box_layout = BoxLayout(
            orientation='horizontal',
            size_hint_y=1,
        )
                            # Elementos da Box de Mana
        self.defense_label = Label(text='defense', size_hint_x=3)
        minus_defense_button = Button(text='-', size_hint_x=1)
        minus_defense_button.bind(on_press=self.minus_defense)

        plus_defense_button = Button(text='+', size_hint_x=1)
        plus_defense_button.bind(on_press=self.plus_defense)

                                # Adicionando os elementos À Caixa de defense
        defense_box_layout.add_widget(minus_defense_button)
        defense_box_layout.add_widget(self.defense_label) # Alterar para receber o valor do defense total
        defense_box_layout.add_widget(plus_defense_button)

                            # Adicionando os elementos à caixa de alterar stats
        change_stats_layout.add_widget(Label(text='Stats',size_hint_y=3))
        change_stats_layout.add_widget(hp_box_layout)
        change_stats_layout.add_widget(mana_box_layout)
        change_stats_layout.add_widget(defense_box_layout)
        change_stats_layout.add_widget(Widget(size_hint_y=2))

                # Box lado direito para botão voltar
        right_box_layout = BoxLayout(
            orientation='vertical',
        )
                # Elementos da return box layout
                    # Caixa do botão retornar
        return_button_box_layout = BoxLayout(
            orientation='horizontal',
            size_hint_x=1
        )
                        # Elementos da caixa do botão retornar
        return_button = Button(text='Voltar')
        return_button.bind(on_press=self.go_to_game)

                            # Adicionando os elementos da return button box layout
        return_button_box_layout.add_widget(Widget(size_hint_x=1))
        return_button_box_layout.add_widget(return_button)

                # Adicionando elementos da right Box Layout
        right_box_layout.add_widget(Widget(size_hint_y=9))
        right_box_layout.add_widget(return_button_box_layout)
        
            # Adicionando os elementos da main layout
        main_layout.add_widget(Widget(size_hint_x=1))
        main_layout.add_widget(change_stats_layout)
        main_layout.add_widget(right_box_layout)

        # Adicionando o main layout à screen
        self.add_widget(main_layout)

    def on_pre_enter(self):
        self.character = App.get_running_app().character
        if not self.character:
            return
        self.update_ui()
        
    def go_to_game(self,instance):
        game_screen = self.manager.get_screen("game")
        game_screen.update_ui()
        self.manager.current = 'game'
        save_character(self.character)

    def plus_hp(self, instance):
        if not self.character:
            return        
        self.character.base_hp += 1
        self.update_ui()
    
    def minus_hp(self, instance):
        if not self.character:
            return
        if self.character.base_hp > 1:
            self.character.base_hp -= 1
            if self.character.hp > self.character.base_hp:
                self.character.hp = self.character.base_hp
            self.update_ui()
    
    def plus_mana(self, instance):
        if not self.character:
            return
        self.character.base_mana += 1
        self.update_ui()

    def minus_mana(self, instance):
        if not self.character:
            return
        if self.character.base_mana > 1:
            self.character.base_mana -= 1
            if self.character.mana > self.character.base_mana:
                self.character.mana = self.character.base_mana
            self.update_ui()

    def plus_defense(self, instance):
        if not self.character:
            return
        self.character.defense += 1
        self.update_ui()

    def minus_defense(self, instance):
        if not self.character:
            return
        if self.character.defense > 10:
            self.character.defense -= 1
            if self.character.defense > self.character.defense:
                self.character.defense = self.character.defense
            self.update_ui()
    
    def update_ui(self):
        if not self.character:
            return
        self.hp_label.text = f'HP {self.character.hp}/{self.character.base_hp}'
        self.mana_label.text = f'Mana {self.character.mana}/{self.character.base_mana}'
        self.defense_label.text = f'Defesa {self.character.defense}'
