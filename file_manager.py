# file_manager.py
# StudyMaster ICS4U Final Project

import json
import os
from deck import Deck

class FileManager:

    @staticmethod
    def save_decks(decks, filename="flashcards.json"):
        data = [deck.to_dict() for deck in decks]

        with open(filename, "w") as file:
            json.dump(data, file, indent=4)

    @staticmethod
    def load_decks(filename="flashcards.json"):
        if not os.path.exists(filename):
            return []

        try:
            with open(filename, "r") as file:
                data = json.load(file)

            return [Deck.from_dict(deck_data) for deck_data in data]

        except:
            return []
