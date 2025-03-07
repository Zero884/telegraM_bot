import json
import random
import os

DATA_FILE = os.path.join(os.path.dirname(__file__), "..", "data.json")

def get_random_quote():
    with open(DATA_FILE, "r", encoding="utf-8") as file:
        quotes = json.load(file)
    return random.choice(quotes)
def add_quote():
    pass

