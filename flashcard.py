# flashcard.py
# StudyMaster ICS4U Final Project
# Authors: Jony & Arseni

class Flashcard:
    """
    Represents a single flashcard.
    """

    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

    def to_dict(self):
        return {
            "question": self.question,
            "answer": self.answer
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            data["question"],
            data["answer"]
        )

    def __str__(self):
        return f"Question: {self.question} | Answer: {self.answer}"
