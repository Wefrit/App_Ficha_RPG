from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from ui.ability_widget import AbilityWidget
from ui.attributes_widgets import AttributesWidget
from kivy.uix.widget import Widget
from characters.characters import *
from kivy.app import App
from save_manager import save_character


class AttributesScreen(Screen):

    def __init__(self, **kw):
        super().__init__(**kw)

        self.character = None
        self.ability_widgets = {}
        self.attributes_widgets = {}

        # Screen Layout
        screen_layout = BoxLayout(
            orientation='horizontal',
            spacing=20,
            padding=20,
        )
        # Componentes da Screen Layout
            # Ability_layout
        self.ability_layout = BoxLayout(
            orientation='vertical',
            size_hint_x=3,
            spacing=20,
            padding=20,
        )

         # Componentes de Ability layout(Lado Esquerdo)
                    # Label 'Habilidades'
        ability_label = Label(
            text='Habilidades',
            size_hint_y=0.1,
            )
                    # New_Ability_layout
        new_ability_layout = BoxLayout(
            orientation='horizontal',
            size_hint_y=0.1,
        )

                    # Caixa BoxLoop
        self.loop_ability_box = BoxLayout(
            orientation='vertical',
            size_hint_y=1,
            spacing=10
        )            
                    # Componentes do New_Ability_layout
                        # New_Ability_box   
        self.new_ability_input = TextInput(
            hint_text='Nova Habilidade',
            multiline=False,
            size_hint_y=1,
        )    
                        # New_Ability_button
        new_ability_button = Button(
            text='+',
            size_hint_y=1
        )
        new_ability_button.bind(on_press=self.update_ability)

        # Ability Layout(Label)[Vertical]
        self.ability_layout.add_widget(ability_label)

        # Box New Ability[Horizontal]
        new_ability_layout.add_widget(self.new_ability_input)
        new_ability_layout.add_widget(new_ability_button)

        # Ability Layout(Box)[Vertical]
        self.ability_layout.add_widget(new_ability_layout)
        self.ability_layout.add_widget(self.loop_ability_box)


            # Att_layout
        self.attribute_layout = BoxLayout(
            orientation='vertical',
            size_hint_x=3,
            spacing=20,
            padding=20
        )

         # Componentes de att layout(Lado Esquerdo)
                    # Label 'Habilidades'
        attribute_label = Label(
            text='Atributos',
            size_hint_y=0.1,
            )
                    # New_attribute_layout
        new_attribute_layout = BoxLayout(
            orientation='horizontal',
            size_hint_y=0.1,
        )

                    # Caixa BoxLoop
        self.loop_attribute_box = BoxLayout(
            orientation='vertical',
            size_hint_y=1,
            spacing=10
        )            
                    # Componentes do New_attribute_layout
                        # New_attribute_box   
        self.new_attribute_input = TextInput(
            hint_text='Novo Atributo',
            multiline=False,
            size_hint_y=1,
        )    
                        # New_attribute_button
        new_attribute_button = Button(
            text='+',
            size_hint_y=1
        )
        new_attribute_button.bind(on_press=self.update_attribute)

        # attribute Layout(Label)[Vertical]
        self.attribute_layout.add_widget(attribute_label)

        # Box New attribute[Horizontal]
        new_attribute_layout.add_widget(self.new_attribute_input)
        new_attribute_layout.add_widget(new_attribute_button)

        # attribute Layout(Box)[Vertical]
        self.attribute_layout.add_widget(new_attribute_layout)
        self.attribute_layout.add_widget(self.loop_attribute_box)

        # Caixa de botão voltar

        return_box_layout = BoxLayout(
            orientation='vertical',
            size_hint_x=1,
        )
            # Elementos da caixa de botão voltar
        return_button = Button(text='Voltar')
        return_button.bind(on_press=self.go_to_options)

                # Adicionando elemtnos ao return box layout
        return_box_layout.add_widget(Widget(size_hint_y=8))
        return_box_layout.add_widget(return_button)
               
        # Screen Layout[Vertical]
        screen_layout.add_widget(Widget(size_hint_x=1))
        screen_layout.add_widget(self.ability_layout)
        screen_layout.add_widget(self.attribute_layout)
        screen_layout.add_widget(return_box_layout)
       
        # Main Screen
        self.add_widget(screen_layout)

    def on_pre_enter(self):
        self.character = App.get_running_app().character
        if not self.character:
            return

        self.loop_ability_box.clear_widgets()
        self.loop_attribute_box.clear_widgets()
        self.ability_widgets = {}
        self.attributes_widgets = {}

        for ability, value in self.character.ability_dict.items():
            widget = AbilityWidget(ability, self)
            widget.value = value
            widget.value_label.text = str(value)
            self.loop_ability_box.add_widget(widget)
            self.ability_widgets[ability] = widget

        for attribute, value in self.character.attribute_dict.items():
            widget = AttributesWidget(attribute, self)
            widget.value = value
            widget.value_label.text = str(value)
            self.loop_attribute_box.add_widget(widget)
            self.attributes_widgets[attribute] = widget
        
    def update_ability(self, instance):
        if not self.character:
            return
        ability = self.new_ability_input.text.strip()
        if not ability:
            return
        if ability not in self.character.ability_dict:
            self.character.ability_dict[ability] = 1
            ability_widget = AbilityWidget(
                ability,
                self
            )
            self.loop_ability_box.add_widget(ability_widget)
            self.ability_widgets[ability] = ability_widget
    
        else:
            widget = self.ability_widgets[ability]
            widget.add_point(None)

        save_character(self.character)
        self.new_ability_input.text = ""
    
    def update_attribute(self, instance):
        if not self.character:
            return
        attribute = self.new_attribute_input.text.strip()
        if not attribute:
            return
        if attribute not in self.character.attribute_dict:
            self.character.attribute_dict[attribute] = 1
            attribute_widget = AttributesWidget(
                attribute,
                self
            )
            self.loop_attribute_box.add_widget(attribute_widget)
            self.attributes_widgets[attribute] = attribute_widget

        else:
            widget = self.attributes_widgets[attribute]
            widget.add_point(None)
            
        save_character(self.character)
        self.new_attribute_input.text = ""

    def go_to_options(self,instace):
        game_screen = self.manager.get_screen("game")
        game_screen.update_ui()
        self.manager.current='options'
