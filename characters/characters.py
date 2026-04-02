class Character:
    default_name = 'Nome'
    def __init__(self, name=None):
        self.save_filename = None
        if not name:
            name = self.default_name
        self.name = name
        self.mana = 0
        self.base_mana = 0
        self.hp = 0
        self.base_hp = 0
        self.xp = 0
        self.lvl = 1
        self.attribute_dict = {'destreza':0,'raciocinio':0}
        self.magic_dict = {}
        self.ability_dict = {}
        self.ability_points = 0
        self.att_points = 0
        self.magic_points = 0
        self.quality_points = 0
        self.defense = 10
        self.annotations = ""


    # Ganhar xp
    def gain_xp(self, amount: int):
        self.xp += amount
        while self.xp >= (self.lvl + 1) * 100:
            self.xp -= (self.lvl + 1) * 100
            self.lvl += 1
            self._level_up()


    def _level_up(self):
        pass

    def take_damage(self, amount: int):
        self.hp = max(0, self.hp - amount)
    
    def heal(self, amount: int):
        self.hp = min(self.base_hp, self.hp + amount)
    
    def use_mana(self, amount: int):
        if self.mana >= amount:
            self.mana -= amount

    def restore_mana(self, amount: int):
        self.mana = min(self.base_mana, self.mana + amount)        
    
    def to_dict(self):
        return {
            "class": self.__class__.__name__,
            "name": self.name,
            "mana": self.mana,
            "base_mana": self.base_mana,
            "hp": self.hp,
            "base_hp": self.base_hp,
            "xp": self.xp,
            "lvl": self.lvl,
            "attribute_dict": self.attribute_dict,
            "magic_dict": self.magic_dict,
            "ability_dict": self.ability_dict,
            "ability_points": self.ability_points,
            "att_points": self.att_points,
            "magic_points": self.magic_points,
            "quality_points": self.quality_points,
            "annotations": self.annotations
        }

    def normalize(self):
        defaults = {
            'destreza': 0,
            'raciocinio': 0
        }

        for key, value in defaults.items():
            self.attribute_dict.setdefault(key, value)

        if not hasattr(self, 'defense'):
            self.defense = 10

    @classmethod
    def from_dict(cls, data):
        class_map = {
            "Bardo": Bardo,
            "Gorgona": Gorgona,
            "Fada": Fada,
            "Golen": Golen,
            "Elfo": Elfo,
            "Vampiro": Vampiro,
            "Panda": Panda,
            "Dríade": Dríade,
            "Draconiano": Draconiano,
            "Who": Who
        }

        character_class = class_map.get(data["class"], Character)
        character = character_class(data["name"])

        character.mana = data["mana"]
        character.base_mana = data["base_mana"]
        character.hp = data["hp"]
        character.base_hp = data["base_hp"]
        character.xp = data["xp"]
        character.lvl = data["lvl"]
        character.attribute_dict = data["attribute_dict"]
        character.magic_dict = data["magic_dict"]
        character.ability_dict = data["ability_dict"]
        character.ability_points = data["ability_points"]
        character.att_points = data["att_points"]
        character.magic_points = data["magic_points"]
        character.quality_points = data["quality_points"]
        character.annotations = data["annotations"]

        return character

# Characters
    # Bardo
class Bardo(Character):
    sprite = "characters/bardo/bardo_base_1.png"
    default_name = 'Fernando'
    def __init__(self, name):
        super().__init__(name)
        self.base_hp = 40
        self.base_mana = 10
        self.hp = 40
        self.mana = 10
        self.ability_points = 0
        self.quality_points = 0
        self.magic_points = 0
        self.att_points = 0

    def _level_up(self):
        # Bardo
        if (self.lvl - 1) % 6 == 0:
            self.base_mana += 2
        if (self.lvl - 1) % 5 == 0:
            self.att_points += 1
        if (self.lvl - 1) % 4 == 0:
            self.magic_points += 1
        if (self.lvl - 1) % 3 == 0:
            self.quality_points += 2
        if self.lvl % 3 == 0:
            self.base_hp += 1
        self.ability_points += 1

    # Gorgona
class Gorgona(Character):
    sprite = "characters/gorgona/gorgona_base_1.png"
    default_name = 'Quezia'
    def __init__(self, name):
        super().__init__(name)
        self.base_hp = 60
        self.base_mana = 10
        self.hp = 60
        self.mana = 10
        self.ability_points = 0
        self.quality_points = 0
        self.magic_points = 0
        self.att_points = 0

    def _level_up(self):
        # Ladina
        if (self.lvl - 1) % 6 == 0:
            self.base_mana += 1
        if (self.lvl - 1) % 5 == 0:
            self.magic_points += 1
        if (self.lvl - 1) % 4 == 0:
            self.att_points += 1
        if (self.lvl - 1) % 3 == 0:
            self.base_hp += 1
        if self.lvl % 3 == 0:
            self.quality_points += 2
        self.ability_points += 2

class Fada(Character):
    default_name = 'Freya'
    sprite = "characters/fada/fada_base_1.png"
    def __init__(self, name):
        super().__init__(name)
        self.base_hp = 20
        self.base_mana = 10
        self.hp = 20
        self.mana = 10
        self.ability_points = 0
        self.quality_points = 0
        self.magic_points = 0
        self.att_points = 0

    def _level_up(self):
        # Clérigo   
        if (self.lvl - 1) % 6 == 0:
            self.base_mana += 2
        if (self.lvl - 1) % 5 == 0:
            self.magic_points += 2
        if (self.lvl - 1) % 4 == 0:
            self.att_points += 1
        if (self.lvl - 1) % 3 == 0:
            self.ability_points += 1
        if self.lvl % 3 == 0:
            self.quality_points += 1
        self.base_hp += 1

class Golen(Character):
    sprite = "characters/golen/golen_base_1.png"
    default_name = 'Felipe'
    def __init__(self, name):
        super().__init__(name)
        self.base_hp = 80
        self.base_mana = 10
        self.hp = 80
        self.mana = 10
        self.ability_points = 0
        self.quality_points = 0
        self.magic_points = 0
        self.att_points = 0

    def _level_up(self):
        # Bárbaro
        if (self.lvl - 1) % 6 == 0:
            self.base_mana += 1
        if (self.lvl - 1) % 5 == 0:
            self.magic_points += 1
        if (self.lvl - 1) % 4 == 0:
            self.att_points += 2
        if (self.lvl - 1) % 3 == 0:
            self.quality_points += 1
        if self.lvl % 3 == 0:
            self.ability_points += 2
        self.base_hp += 1

class Elfo(Character):
    sprite = "characters/elfo/elfo_base_1.png"
    default_name = 'Carol'

    def __init__(self, name):
        super().__init__(name)
        self.base_hp = 40
        self.base_mana = 10
        self.hp = 40
        self.mana = 10
        self.ability_points = 0
        self.quality_points = 0
        self.magic_points = 0
        self.att_points = 0

    def _level_up(self):
        # Mago
        if (self.lvl - 1) % 6 == 0:
            self.base_mana += 2
        if (self.lvl - 1) % 5 == 0:
            self.att_points += 1
        if (self.lvl - 1) % 4 == 0:
            self.magic_points += 2
        if (self.lvl - 1) % 3 == 0:
            self.quality_points += 1
        if self.lvl % 3 == 0:
            self.base_hp += 1
        self.ability_points += 1

class Vampiro(Character):
    sprite = "characters/vampiro/vampiro_base_1.png"
    default_name = 'Julie'

    def __init__(self, name):
        super().__init__(name)
        self.base_hp = 40
        self.base_mana = 10
        self.hp = 40
        self.mana = 10
        self.ability_points = 0
        self.quality_points = 0
        self.magic_points = 0
        self.att_points = 0

    def _level_up(self):
        # Caçadora
        if (self.lvl - 1) % 6 == 0:
            self.base_mana += 1
        if (self.lvl - 1) % 5 == 0:
            self.magic_points += 1
        if (self.lvl - 1) % 4 == 0:
            self.att_points += 2
        if (self.lvl - 1) % 3 == 0:
            self.base_hp += 1
        if self.lvl % 3 == 0:
            self.quality_points += 2
        self.ability_points += 1

class Panda(Character):
    sprite = "characters/panda/panda_base_1.png"
    default_name = 'Luna'

    def __init__(self, name):
        super().__init__(name)
        self.base_hp = 60
        self.base_mana = 10
        self.hp = 60
        self.mana = 10
        self.ability_points = 0
        self.quality_points = 0
        self.magic_points = 0
        self.att_points = 0

    def _level_up(self):
        # Bárbaro
        if (self.lvl - 1) % 6 == 0:
            self.base_mana += 1
        if (self.lvl - 1) % 5 == 0:
            self.magic_points += 1
        if (self.lvl - 1) % 4 == 0:
            self.att_points += 2
        if (self.lvl - 1) % 3 == 0:
            self.quality_points += 1
        if self.lvl % 3 == 0:
            self.ability_points += 1
        self.base_hp += 2

class Dríade(Character):
    sprite = "characters/driade/driade_base_1.png"
    default_name = 'Jessica'
    
    def __init__(self, name):
        super().__init__(name)
        self.base_hp = 40
        self.base_mana = 10
        self.hp = 40
        self.mana = 10
        self.ability_points = 0
        self.quality_points = 0
        self.magic_points = 0
        self.att_points = 0

    def _level_up(self):
        # Druida
        if (self.lvl - 1) % 6 == 0:
            self.base_mana += 2
        if (self.lvl - 1) % 5 == 0:
            self.att_points += 1
        if (self.lvl - 1) % 4 == 0:
            self.magic_points += 1
        if (self.lvl - 1) % 3 == 0:
            self.quality_points += 1
        if self.lvl % 3 == 0:
            self.ability_points += 1
        self.base_hp += 2

class Draconiano(Character):
    sprite = "characters/draconiano/draconiano_base_1.png"
    default_name = 'Paloma'

    def __init__(self, name):
        super().__init__(name)
        self.base_hp = 60
        self.base_mana = 10
        self.hp = 60
        self.mana = 10
        self.ability_points = 0
        self.quality_points = 0
        self.magic_points = 0
        self.att_points = 0

    def _level_up(self):
        # Paladino
        if (self.lvl - 1) % 6 == 0:
            self.base_mana += 1
        if (self.lvl - 1) % 5 == 0:
            self.magic_points += 2
        if (self.lvl - 1) % 4 == 0:
            self.att_points += 1
        if (self.lvl - 1) % 3 == 0:
            self.quality_points += 1
        if self.lvl % 3 == 0:
            self.base_hp += 2
        self.ability_points += 1

class Who(Character):
    sprite = "characters/who/who_base_1.png"
    default_name = 'Catarina/Luke'

    def __init__(self, name):
        super().__init__(name)
        self.base_hp = 10
        self.base_mana = 10
        self.hp = 10
        self.mana = 10
        self.ability_points = 0
        self.quality_points = 0
        self.magic_points = 0
        self.att_points = 0

    def _level_up(self):
        # Cavaleiro
        if (self.lvl - 1) % 6 == 0:
            self.base_mana += 1
        if (self.lvl - 1) % 5 == 0:
            self.magic_points += 1
        if (self.lvl - 1) % 4 == 0:
            self.att_points += 1
        if (self.lvl - 1) % 3 == 0:
            self.quality_points += 1
        if self.lvl % 3 == 0:
            self.base_hp += 2
        self.ability_points += 2
