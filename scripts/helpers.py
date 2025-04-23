import json 

def load_settings():
    with open('config/settings.json') as f:
        settings = json.load(f)