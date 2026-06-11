# deck.py
# StudyMaster ICS4U Final Project

from flashcard import Flashcard

class Deck:
    """
    Stores and manages a collection of flashcards.
    """

    def __init__(self, name):
        self.name = name
        self.flashcards = []

    def add_flashcard(self, question, answer):
        card = Flashcard(question, answer)
        self.flashcards.append(card)

    def remove_flashcard(self, index):
        if 0 <= index < len(self.flashcards):
            self.flashcards.pop(index)

    def get_flashcards(self):
        return self.flashcards

    def to_dict(self):
        return {
            "name": self.name,
            "flashcards": [card.to_dict() for card in self.flashcards]
        }

    @classmethod
    def from_dict(cls, data):
        deck = cls(data["name"])

        for card_data in data["flashcards"]:
            deck.flashcards.append(
                Flashcard.from_dict(card_data)
            )

        return deck

    def __len__(self):
        return len(self.flashcards)
