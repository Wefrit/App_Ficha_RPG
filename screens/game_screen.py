from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget
from kivy.uix.popup import Popup
from kivy.app import App
from characters.characters import *
from save_manager import save_character

class GameScreen(Screen):


    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.character = None
        self.character_sprite = None
        self.build_ui()

    def on_pre_enter(self):
        self.character = App.get_running_app().character

        if not self.character:
            return

        self.character_sprite.source = self.character.sprite
        self.update_ui()

    def build_ui(self):
        # Layouts
            # Principal (Toda a tela)
        main_layout = BoxLayout(
            orientation='horizontal',
            padding=20,
            spacing=10,
            )
        
            # Lado esquerdo da tela
        left_layout = BoxLayout(
            orientation='vertical',
            size_hint_x=1,
        )

        mid_layout = BoxLayout(
            orientation='vertical',
            size_hint_x=1,
            spacing=10,
            padding=10,
        )

        right_layout = BoxLayout(
            orientation='vertical',
            size_hint_x=1,
        )

        # Componentes dos layouts
            #  Left Layout (top)
                # Labels
                    # Label status
        STATS = Label(size_hint_y=2, text='Stats')
        self.level_label = Label(size_hint_y=1)
        self.xp_label = Label(size_hint_y=1)
        self.hp_label = Label(size_hint_y=1)
        self.mana_label = Label(size_hint_y=1)
        self.att_label = Label(size_hint_y=1)
        self.magic_label = Label(size_hint_y=1)
        self.ability_label = Label(size_hint_y=1)
        self.quality_label = Label(size_hint_y=1)
        

            # Left Layout widgets
        left_layout.add_widget(STATS)
        left_layout.add_widget(self.level_label)
        left_layout.add_widget(self.xp_label)
        left_layout.add_widget(self.hp_label)
        left_layout.add_widget(self.mana_label)
        left_layout.add_widget(self.att_label)
        left_layout.add_widget(self.magic_label)
        left_layout.add_widget(self.ability_label)
        left_layout.add_widget(self.quality_label)

            # Left Layout (Bottom)
        self.note_box_button = Button(text='Criar Anotação')
        self.note_box_button.bind(on_press=self.open_annotation)
        left_layout.add_widget(self.note_box_button)

            # Mid Layout
                # Labels
                    # Label status
        self.name_label= Label(size_hint_y=0.1)

                # Sprite Personagem
        self.character_sprite = Image(
            source="",
            size_hint_y=0.8,
            allow_stretch=True,
            keep_ratio=True,
        )

                # Botões
                    # Botão ganhar xp
                        # layout do botão xp
        self.gain_xp_layout = BoxLayout(
            size_hint_y=0.1,
            orientation='horizontal'
        )

        self.gain_xp_input = TextInput(
            hint_text='Ganhar XP',
            input_filter='int',
            size_hint_y=1,
            size_hint_x=0.8,
        )
        self.gain_xp_button = Button(
            text='XP',
            size_hint_x=0.2,
            size_hint_y=1,
        )
        self.gain_xp_button.bind(on_press=self.gain_xp)
        
        self.gain_xp_layout.add_widget(self.gain_xp_input)
        self.gain_xp_layout.add_widget(self.gain_xp_button)
            # Mid Layout Widgets
        mid_layout.add_widget(self.name_label)
        mid_layout.add_widget(self.character_sprite)
        mid_layout.add_widget(self.gain_xp_layout)
        
        # Right Layout
            # Top
        top_right_box = BoxLayout(
            size_hint_y=0.5,
            spacing=20,
            padding=50
        )
                # Botões de cima
                    # Voltar
        self.return_button = Button(
            text='Voltar',
            size_hint_x=0.5,
        )
        self.return_button.bind(on_press=self.go_to_menu)

                    # Opções
        self.options_button = Button(
            text='Opções',
            size_hint_x=0.5
        )
        self.options_button.bind(on_press=self.go_to_options)
        top_right_box.add_widget(self.options_button)
        top_right_box.add_widget(self.return_button)

                # Caixa de botões 
        self.button_box = BoxLayout(
            orientation='vertical',
            padding=10,
            spacing=10,
            size_hint_x=1,
        )
                # Componentes da caixa de botões
                    # Caixa de botões de cima
        self.upper_button_box = BoxLayout(
            orientation='horizontal',
            size_hint_y=1,
        )
                    # Botões da caixa de botões de cima
                            # Botão de ganhar hp
        self.hp_up_button = Button(
            text='+ 1 HP',
            size_hint_y=1,
            size_hint_x=1,
        )
        self.hp_up_button.bind(on_press=self.hp_up)

                # Widget Caixa de Botões de cima
        self.upper_button_box.add_widget(Widget(size_hint_x=1,size_hint_y=1))
        self.upper_button_box.add_widget(self.hp_up_button)
        self.upper_button_box.add_widget(Widget(size_hint_x=1,size_hint_y=1))

                    # Caixa de botões do meio
        self.mid_button_box = BoxLayout(
            orientation='horizontal',
            padding=10,
            spacing=10,
            size_hint_y=1,
        )
                    # Botões da caixa de botões do meio
                             # Botão de ganhar mana
        self.mana_up_button = Button(
            text='+ 1 Mana',
            size_hint_y=1,
            size_hint_x=1,
        )
        self.mana_up_button.bind(on_press=self.mana_up)

                            # Botão de perder mana
        self.mana_down_button = Button(
            text='- 1 Mana',
            size_hint_y=1,
            size_hint_x=1,
        )
        self.mana_down_button.bind(on_press=self.mana_down)
             
                # Widgets da Caixa de botões de baixo
        self.mid_button_box.add_widget(self.mana_down_button)
        self.mid_button_box.add_widget(self.mana_up_button)

            # Caixa de botões de baixo
        self.bottom_button_box = BoxLayout(
            orientation='horizontal',
            size_hint_y=1,
        )
                    # Botões da caixa de botões de baixo
                            # Botão de perder hp
        self.hp_down_button = Button(
            text='- 1 HP',
            size_hint_y=1,
            size_hint_x=1,
        )
        self.hp_down_button.bind(on_press=self.hp_down)

                # Widget Caixa de Botões de baixo
        self.bottom_button_box.add_widget(Widget(size_hint_x=1,size_hint_y=1))
        self.bottom_button_box.add_widget(self.hp_down_button)
        self.bottom_button_box.add_widget(Widget(size_hint_x=1,size_hint_y=1))

            # Widgets da caixa de botões
        self.button_box.add_widget(self.upper_button_box)
        self.button_box.add_widget(self.mid_button_box)
        self.button_box.add_widget(self.bottom_button_box)

        # Right Layout Widgets
        right_layout.add_widget(top_right_box)
        right_layout.add_widget(self.button_box)

            # Main Layout
        main_layout.add_widget(left_layout)
        main_layout.add_widget(mid_layout)
        main_layout.add_widget(right_layout)

        self.update_ui()
        self.add_widget(main_layout)
    
    # Fuções
        # Atualizar UI
    def update_ui(self):
        if not self.character:
            return
        self.name_label.text = f'Nome: {self.character.name}'
        self.level_label.text = f'Lvl: {self.character.lvl}'
        self.xp_label.text = f'XP: {self.character.xp}'
        self.hp_label.text = f'HP: {self.character.hp}/{self.character.base_hp}'
        self.mana_label.text = f'Mana: {self.character.mana}/{self.character.base_mana}'
        self.ability_label.text = f'Pontos de Habilidade: {self.character.ability_points}'
        self.att_label.text = f'Pontos de Atributo: {self.character.att_points}'
        self.magic_label.text = f'Pontos de Poder: {self.character.magic_points}'
        self.quality_label.text = f'Pontos de Qualidade {self.character.quality_points}'
        save_character(self.character)

        # Botões
            # Botão ganhar xp
    def gain_xp(self, value):
        value = self.gain_xp_input.text.strip()
        self.character.gain_xp(int(value))
        self.gain_xp_input.text = ''
        self.update_ui()
    
            # Botão recuperar vida
    def hp_up(self, instance):
        self.character.heal(1)
        self.update_ui()

            # Botão perder vida
    def hp_down(self, instance):
        self.character.take_damage(1)
        self.update_ui()

            # Botão recuperar mana
    def mana_up(self, instance):
        self.character.restore_mana(1)
        self.update_ui()

            # Botão perder mana
    def mana_down(self, instance):
        self.character.use_mana(1)
        self.update_ui()

            # Botão retornar
    def go_to_menu(self,instance):
        self.manager.current = "menu"
        save_character(self.character)
    
    def go_to_options(self, instance):
        self.manager.current = "options"

    def open_annotation(self, instance):
        annotation_layout = BoxLayout(orientation='vertical', spacing=10, padding=20)
        annotation_input = TextInput(
            hint_text='Anotações',
            size_hint_y=0.8,
            text=self.character.annotations  # Carrega as anotações salvas
        )

        popup = Popup(
            title='Anotações',
            content=annotation_layout,
            size_hint=(0.8, 0.8)
        )

        close_button = Button(text='Fechar', size_hint_y=0.2)
        close_button.bind(
            on_press=lambda instance: self.close_annotations(instance, popup, annotation_input)
        )
        annotation_layout.add_widget(annotation_input)
        annotation_layout.add_widget(close_button)
        popup.open()

    def close_annotations(self, instance, popup, annotation_input):
        self.character.annotations = annotation_input.text
        save_character(self.character)
        popup.dismiss()