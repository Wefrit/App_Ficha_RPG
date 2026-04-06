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
    import inspect
    import characters.characters as chars

    app = App.get_running_app()
    path = os.path.join(app.user_data_dir, filename)

    if not os.path.exists(path):
        return None

    with open(path, "r") as file:
        data = json.load(file)

    class_name = data.get("class_name")

    if not class_name:
        class_name = filename.split("_")[0]

    # encontrar classe
    classe = None
    for name, obj in inspect.getmembers(chars):
        if inspect.isclass(obj) and name == class_name:
            classe = obj
            break

    if classe is None:
        print(f"Classe {class_name} não encontrada")
        return None

    character = classe(data.get("name", "SemNome"))

    character.__dict__.update(data)

    character.save_filename = filename

    return character

def list_saves():
    app = App.get_running_app()
    files = os.listdir(app.user_data_dir)

    saves = [f for f in files if f.endswith(".json")]
    return saves
