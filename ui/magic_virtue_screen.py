from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from ui.magic_widget import MagicWidget
from ui.virtues_widget import VirtuesWidget
from kivy.uix.widget import Widget
from characters.characters import *
from kivy.app import App
from save_manager import save_character


class MagicVirtuesScreen(Screen):

    def __init__(self, **kw):
        super().__init__(**kw)

        self.character = None
        self.magic_widgets = {}
        self.virtues_widgets = {}

        # Screen Layout
        screen_layout = BoxLayout(
            orientation='horizontal',
            spacing=20,
            padding=20,
        )
        # Componentes da Screen Layout
            # magic_layout
        self.magic_layout = BoxLayout(
            orientation='vertical',
            size_hint_x=3,
            spacing=20,
            padding=20,
        )

         # Componentes de magic layout(Lado Esquerdo)
                    # Label 'Habilidades'
        magic_label = Label(
            text='Poderes',
            size_hint_y=0.1,
            )
                    # New_magic_layout
        new_magic_layout = BoxLayout(
            orientation='horizontal',
            size_hint_y=0.1,
        )

                    # Caixa BoxLoop
        self.loop_magic_box = BoxLayout(
            orientation='vertical',
            size_hint_y=1.2,
            spacing=20
        )            
                    # Componentes do New_magic_layout
                        # New_magic_box   
        self.new_magic_input = TextInput(
            hint_text='Novo Poder',
            multiline=False,
            size_hint_y=1.2,
        )    
                        # New_magic_button
        new_magic_button = Button(
            text='+',
            size_hint_y=1
        )
        new_magic_button.bind(on_press=self.update_magic)

        # magic Layout(Label)[Vertical]
        self.magic_layout.add_widget(magic_label)

        # Box New magic[Horizontal]
        new_magic_layout.add_widget(self.new_magic_input)
        new_magic_layout.add_widget(new_magic_button)

        # magic Layout(Box)[Vertical]
        self.magic_layout.add_widget(new_magic_layout)
        self.magic_layout.add_widget(self.loop_magic_box)


            # Att_layout
        self.virtues_layout = BoxLayout(
            orientation='vertical',
            size_hint_x=3,
            spacing=20,
            padding=20
        )

         # Componentes de att layout(Lado Esquerdo)
                    # Label 'Habilidades'
        virtues_label = Label(
            text='Virtudes',
            size_hint_y=0.1,
            )

                    # Caixa BoxLoop
        self.loop_virtues_box = BoxLayout(
            orientation='vertical',
            size_hint_y=1.2,
            spacing=20
        )            

        # virtues Layout(Label)[Vertical]
        self.virtues_layout.add_widget(virtues_label)

        # virtues Layout(Box)[Vertical]
        self.virtues_layout.add_widget(self.loop_virtues_box)

        screen_layout.add_widget(self.magic_layout)
        screen_layout.add_widget(self.virtues_layout)
       
        # Main Screen
        self.add_widget(screen_layout)

    def on_pre_enter(self):
        self.character = App.get_running_app().character
        if not self.character:
            return

        self.loop_magic_box.clear_widgets()
        self.loop_virtues_box.clear_widgets()
        self.magic_widgets = {}
        self.virtues_widgets = {}

        for magic, value in self.character.magic_dict.items():
            widget = MagicWidget(magic, self)
            widget.value = value
            widget.value_label.text = str(value)
            self.loop_magic_box.add_widget(widget)
            self.magic_widgets[magic] = widget

        for virtues, value in self.character.virtues_dict.items():
            widget = VirtuesWidget(virtues, self)
            widget.value = value
            widget.value_label.text = str(value)
            self.loop_virtues_box.add_widget(widget)
            self.virtues_widgets[virtues] = widget
        
    def update_magic(self, instance):
        if not self.character:
            return
        magic = self.new_magic_input.text.strip()
        if not magic:
            return
        if magic not in self.character.magic_dict:
            self.character.magic_dict[magic] = 1
            magic_widget = MagicWidget(
                magic,
                self
            )
            self.loop_magic_box.add_widget(magic_widget)
            self.magic_widgets[magic] = magic_widget
    
        else:
            widget = self.magic_widgets[magic]
            widget.add_point(None)

        save_character(self.character)
        self.new_magic_input.text = ""
    
    def update_virtues(self, instance):
        if not self.character:
            return
        virtues = self.new_virtues_input.text.strip()
        if not virtues:
            return
        if virtues not in self.character.virtues_dict:
            self.character.virtues_dict[virtues] = 1
            virtues_widget = VirtuesWidget(
                virtues,
                self
            )
            self.loop_virtues_box.add_widget(virtues_widget)
            self.virtues_widgets[virtues] = virtues_widget

        else:
            widget = self.virtues_widgets[virtues]
            widget.add_point(None)
            
        save_character(self.character)
        self.new_virtues_input.text = ""
