# quiz_manager.py
# StudyMaster ICS4U Final Project

import random

class QuizManager:

    def __init__(self, deck):
        self.deck = deck
        self.score = 0

    def get_questions(self):
        cards = self.deck.get_flashcards().copy()
        random.shuffle(cards)
        return cards

    def check_answer(self, user_answer, correct_answer):
        if user_answer.strip().lower() == correct_answer.strip().lower():
            self.score += 1
            return True

        return False

    def get_score(self):
        return self.score

    def reset_score(self):
        self.score = 0
