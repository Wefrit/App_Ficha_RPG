from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from save_manager import save_character


class AbilityWidget(BoxLayout):

    def __init__(self, ability_name, screen, **kwargs):
        super().__init__(orientation='horizontal', **kwargs)

        self.ability_name = ability_name
        self.screen = screen
        self.value = 1

        # Label do nome
        self.name_label = Label(
            text=ability_name,
            size_hint_x=0.6
        )

        # Label do valor
        self.value_label = Label(
            text="1",
            size_hint_x=0.2
        )

        # Botões
        minus_button = Button(text='-', size_hint_x=0.1)
        minus_button.bind(on_press=self.lose_point)
        plus_button = Button(text='+', size_hint_x=0.1)
        plus_button.bind(on_press=self.add_point)

        # Adiciona na linha
        self.add_widget(self.name_label)
        self.add_widget(minus_button)
        self.add_widget(self.value_label)
        self.add_widget(plus_button)

    def add_point(self, instance):
        self.value += 1
        self.value_label.text = str(self.value)
        self.screen.character.ability_dict[self.ability_name] = self.value
        save_character(self.screen.character)

    def lose_point(self, instance):
        self.value -= 1
        if self.value <= 0:
            del self.screen.character.ability_dict[self.ability_name]
            self.screen.loop_ability_box.remove_widget(self)
        else:
            self.value_label.text = str(self.value)
            self.screen.character.ability_dict[self.ability_name] = self.value
        save_character(self.screen.character)
        