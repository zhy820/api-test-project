import os
import yaml

from parametrize import BASE_URL

CONFIG_DIR = os.path.dirname(os.path.abspath(__file__))
CONFIG_FILE = os.path.join(CONFIG_DIR, 'config.yaml')

def load_config():
    with open(CONFIG_FILE, 'r', encoding="utf-8") as f:
        return yaml.safe_load(f)


config = load_config()

BASE_URL = config["base"]["url"]
USERNAME = config["user"]["username"]
PASSWORD = config["user"]["password"]
