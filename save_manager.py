import json
import os
from kivy.app import App
from characters.characters import Character


def save_character(character):
    app = App.get_running_app()

    if hasattr(character, "save_filename") and character.save_filename:
        filename = character.save_filename
    else:
        class_name = character.__class__.__name__
        base_filename = f"{class_name}_{character.name}"
        filename = base_filename + ".json"

    path = os.path.join(app.user_data_dir, filename)

    data = character.to_dict()

    with open(path, "w") as file:
        json.dump(data, file)

    character.save_filename = filename

def load_character(filename):
    app = App.get_running_app()
    path = os.path.join(app.user_data_dir, filename)

    if not os.path.exists(path):
        return None

    with open(path, "r") as file:
        data = json.load(file)

    character = Character.from_dict(data)

    character.save_filename = filename

    return character

def list_saves():
    app = App.get_running_app()
    files = os.listdir(app.user_data_dir)

    saves = [f for f in files if f.endswith(".json")]
    return saves
