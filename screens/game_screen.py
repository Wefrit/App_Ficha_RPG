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
from ui.attributes_screen import AttributesScreen
from ui.magic_virtue_screen import MagicVirtuesScreen
from save_manager import save_character
from kivy.metrics import dp

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
        self.defense_label = Label(size_hint_y=1)
        self.initiative_label = Label(size_hint_y=1)
        
        self.attributes_abilities_button = Button(size_hint_y=1, text='Atributos/Habilidades')
        self.attributes_abilities_button.bind(on_press=self.open_attributes_abilities)
        self.powers_virtues_button = Button(size_hint_y=1, text='Poderes/Virtudes')
        self.powers_virtues_button.bind(on_press=self.open_powers_virtues)

            # Left Layout widgets
        left_layout.add_widget(STATS)
        left_layout.add_widget(self.level_label)
        left_layout.add_widget(self.xp_label)
        left_layout.add_widget(self.hp_label)
        left_layout.add_widget(self.mana_label)
        left_layout.add_widget(self.defense_label)
        left_layout.add_widget(self.initiative_label)
        left_layout.add_widget(self.attributes_abilities_button)
        left_layout.add_widget(self.powers_virtues_button)
        
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
            size_hint_y=0.3,
            spacing=20,
            padding=20
        )
                # Status
        self.stats_button = Button(
            text='Status',
            size_hint_x=1
        )
        self.stats_button.bind(on_press=self.go_to_stats)
        top_right_box.add_widget(self.stats_button)
            
            # Mid
                # Caixa de botões 
        self.button_box = BoxLayout(
            orientation='vertical',
            padding=[5, 10, 10, 1],
            spacing=10,
            size_hint_x=1,
        )
                # Componentes da caixa de botões
                    # Caixa de botões de cima
        self.upper_button_box = BoxLayout(
            orientation='horizontal',
            size_hint_y=None,
            height=dp(100),
            spacing=10,
            padding=10
        )
                    # Botões da caixa de botões de cima
                            # Botão de ganhar hp
        self.hp_up_button = Button(
            text='+ 1 hp',
            size_hint=(None, None),
            size=(dp(80), dp(80)),
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
            size_hint_y=None,
            height=dp(100),
        )
                    # Botões da caixa de botões do meio
                             # Botão de ganhar mana
        self.mana_up_button = Button(
            text='+ 1 Mana',
            size_hint=(None, None),
            size=(dp(80), dp(80)),
        )
        self.mana_up_button.bind(on_press=self.mana_up)

                            # Botão de perder mana
        self.mana_down_button = Button(
            text='- 1 Mana',
            size_hint=(None, None),
            size=(dp(80), dp(80)),
        )
        self.mana_down_button.bind(on_press=self.mana_down)
             
                # Widgets da Caixa de botões de baixo
        self.mid_button_box.add_widget(Widget(size_hint_x=1))
        self.mid_button_box.add_widget(self.mana_down_button)
        self.mid_button_box.add_widget(Widget(size_hint_x=0.2))
        self.mid_button_box.add_widget(self.mana_up_button)
        self.mid_button_box.add_widget(Widget(size_hint_x=1))

            # Caixa de botões de baixo
        self.bottom_button_box = BoxLayout(
            orientation='horizontal',
            size_hint_y=None,
            height=dp(100),
            padding=10,
            spacing=10,
        )
                    # Botões da caixa de botões de baixo
                            # Botão de perder hp
        self.hp_down_button = Button(
            text='- 1 HP',
            size_hint=(None, None),
            size=(dp(80), dp(80)),
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

            # Bot Right
                # Return Box
        bot_right_box = BoxLayout(
            orientation='horizontal',
            size_hint_y=0.5,
            spacing=20,
            padding=10,
        )
                    # Voltar
        self.return_button = Button(
            text='Sair',
            size_hint_x=1,
        )
        self.return_button.bind(on_press=self.go_to_menu)

        return_container = BoxLayout(orientation='vertical')

        return_container.add_widget(Widget())  # empurra pra baixo
        return_container.add_widget(self.return_button)

        bot_right_box.add_widget(Widget())  # empurra pra direita
        bot_right_box.add_widget(return_container)

        # Right Layout Widgets
        right_layout.add_widget(top_right_box)
        right_layout.add_widget(Widget(size_hint_y=0.3))
        right_layout.add_widget(self.button_box)
        right_layout.add_widget(bot_right_box)

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
        self.defense_label.text = f'Defesa: {self.character.defense}'
        self.initiative_label.text = f"Iniciativa: {self.character.attribute_dict['destreza'] + self.character.attribute_dict['raciocinio']}"
        save_character(self.character)

        # Botões
            # Botão ganhar xp
    def gain_xp(self, instance):
        value = self.gain_xp_input.text.strip()
        if not value:
            return

        value = int(value)

        old_stats = {
            "lvl": self.character.lvl,
            "hp": self.character.base_hp,
            "mana": self.character.base_mana,
            "att": self.character.att_points,
            "magic": self.character.magic_points,
            "quality": self.character.quality_points,
            "ability": self.character.ability_points
        }

        self.character.gain_xp(value)

        self.gain_xp_input.text = ''

        self.check_level_up(old_stats)

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
    
    def go_to_stats(self, instance):
        self.manager.current = "stats"

    def open_annotation(self, instance):
        annotation_layout = BoxLayout(orientation='vertical', spacing=10, padding=20)
        annotation_input = TextInput(
            hint_text='Anotações',
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

    def open_attributes_abilities(self, instance):
        # layout principal do popup
        root_layout = BoxLayout(orientation='vertical')

        # conteúdo da tela
        content = AttributesScreen()
        content.character = App.get_running_app().character
        content.on_pre_enter()

        # botão fechar
        close_button = Button(text='Fechar', size_hint_y=0.1)
        
        popup = Popup(
            title='Atributos e Habilidades',
            size_hint=(0.8, 0.8)
        )

        close_button.bind(on_press=lambda instance: self.close_popup(popup))

        # adiciona tudo dentro de um único layout
        root_layout.add_widget(content)
        root_layout.add_widget(close_button)

        # define esse layout como conteúdo do popup
        popup.content = root_layout

        popup.open()
        self.update_ui()
    
    def close_popup(self, popup):
        popup.dismiss()
        self.update_ui()

    def open_powers_virtues(self, instance):
        # layout principal do popup
        root_layout = BoxLayout(orientation='vertical')

        # conteúdo da tela
        content = MagicVirtuesScreen()
        content.character = App.get_running_app().character
        content.on_pre_enter()

        # botão fechar
        close_button = Button(text='Fechar', size_hint_y=0.1)
        
        popup = Popup(
            title='Poderes e Virtudes',
            size_hint=(0.8, 0.8)
        )

        close_button.bind(on_press=lambda instance: self.close_popup(popup))

        # adiciona tudo dentro de um único layout
        root_layout.add_widget(content)
        root_layout.add_widget(close_button)

        # define esse layout como conteúdo do popup
        popup.content = root_layout

        popup.open()
        self.update_ui()

    def check_level_up(self, old_stats):
        new_stats = {
            "lvl": self.character.lvl,
            "hp": self.character.base_hp,
            "mana": self.character.base_mana,
            "att": self.character.att_points,
            "magic": self.character.magic_points,
            "quality": self.character.quality_points,
            "ability": self.character.ability_points
        }

        # se não subiu nível, ignora
        if new_stats["lvl"] == old_stats["lvl"]:
            return

        ganhos = []

        if new_stats["hp"] > old_stats["hp"]:
            ganhos.append(f"+{new_stats['hp'] - old_stats['hp']} HP Base")

        if new_stats["mana"] > old_stats["mana"]:
            ganhos.append(f"+{new_stats['mana'] - old_stats['mana']} Mana Base")

        if new_stats["att"] > old_stats["att"]:
            ganhos.append(f"+{new_stats['att'] - old_stats['att']} Pontos de Atributo")

        if new_stats["magic"] > old_stats["magic"]:
            ganhos.append(f"+{new_stats['magic'] - old_stats['magic']} Pontos de Magia")

        if new_stats["quality"] > old_stats["quality"]:
            ganhos.append(f"+{new_stats['quality'] - old_stats['quality']} Pontos de Qualidade")

        if new_stats["ability"] > old_stats["ability"]:
            ganhos.append(f"+{new_stats['ability'] - old_stats['ability']} Pontos de Habilidade")

        self.show_level_up_popup(old_stats["lvl"], new_stats["lvl"], ganhos)

    def show_level_up_popup(self, old_lvl, new_lvl, ganhos):
        from kivy.uix.popup import Popup
        from kivy.uix.boxlayout import BoxLayout
        from kivy.uix.label import Label
        from kivy.uix.button import Button

        layout = BoxLayout(orientation='vertical', spacing=10, padding=20)

        texto = f"Subiu de nível!\n{old_lvl} → {new_lvl}\n\n"

        if ganhos:
            texto += "\n".join(ganhos)
        else:
            texto += "Sem ganhos adicionais"

        label = Label(text=texto)

        close_btn = Button(text="OK", size_hint_y=0.3)

        popup = Popup(
            title="Level Up!",
            content=layout,
            size_hint=(0.7, 0.5)
        )

        close_btn.bind(on_press=popup.dismiss)

        layout.add_widget(label)
        layout.add_widget(close_btn)

        popup.open()