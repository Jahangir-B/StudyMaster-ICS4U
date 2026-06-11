# statistics_manager.py
# StudyMaster ICS4U Final Project

import json
import os

class StatisticsManager:

    def __init__(self):
        self.quizzes_taken = 0
        self.total_score = 0
        self.highest_score = 0

    def add_score(self, score):
        self.quizzes_taken += 1
        self.total_score += score

        if score > self.highest_score:
            self.highest_score = score

    def get_average(self):
        if self.quizzes_taken == 0:
            return 0

        return round(self.total_score / self.quizzes_taken, 2)

    def save(self, filename="statistics.json"):
        data = {
            "quizzes_taken": self.quizzes_taken,
            "total_score": self.total_score,
            "highest_score": self.highest_score
        }

        with open(filename, "w") as file:
            json.dump(data, file, indent=4)

    def load(self, filename="statistics.json"):
        if not os.path.exists(filename):
            return

        try:
            with open(filename, "r") as file:
                data = json.load(file)

            self.quizzes_taken = data.get("quizzes_taken", 0)
            self.total_score = data.get("total_score", 0)
            self.highest_score = data.get("highest_score", 0)

        except:
            pass
