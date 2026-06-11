# main.py
# StudyMaster ICS4U Final Project

import tkinter as tk
from tkinter import messagebox, simpledialog

from deck import Deck
from file_manager import FileManager
from quiz_manager import QuizManager
from statistics_manager import StatisticsManager


class StudyMasterGUI:

    def __init__(self, root):
        self.root = root
        self.root.title("StudyMaster")
        self.root.geometry("700x500")

        self.decks = FileManager.load_decks()
        self.stats = StatisticsManager()
        self.stats.load()

        self.current_deck = None

        self.build_main_screen()

    def build_main_screen(self):

        for widget in self.root.winfo_children():
            widget.destroy()

        title = tk.Label(
            self.root,
            text="StudyMaster",
            font=("Arial", 22, "bold")
        )
        title.pack(pady=20)

        tk.Button(
            self.root,
            text="Create Deck",
            width=20,
            command=self.create_deck
        ).pack(pady=5)

        tk.Button(
            self.root,
            text="Open Deck",
            width=20,
            command=self.open_deck
        ).pack(pady=5)

        tk.Button(
            self.root,
            text="Quiz Mode",
            width=20,
            command=self.start_quiz
        ).pack(pady=5)

        tk.Button(
            self.root,
            text="Statistics",
            width=20,
            command=self.show_stats
        ).pack(pady=5)

        tk.Button(
            self.root,
            text="Save",
            width=20,
            command=self.save_all
        ).pack(pady=5)

        tk.Button(
            self.root,
            text="Exit",
            width=20,
            command=self.exit_program
        ).pack(pady=5)

    def create_deck(self):

        name = simpledialog.askstring(
            "Create Deck",
            "Enter deck name:"
        )

        if name:
            deck = Deck(name)
            self.decks.append(deck)

            messagebox.showinfo(
                "Success",
                "Deck created successfully."
            )

    def open_deck(self):

        if not self.decks:
            messagebox.showwarning(
                "No Decks",
                "Create a deck first."
            )
            return

        names = [deck.name for deck in self.decks]

        selected = simpledialog.askstring(
            "Open Deck",
            "Available Decks:\n\n" +
            "\n".join(names) +
            "\n\nEnter deck name:"
        )

        for deck in self.decks:
            if deck.name == selected:
                self.current_deck = deck
                self.deck_menu()
                return

        messagebox.showerror(
            "Error",
            "Deck not found."
        )

    def deck_menu(self):

        for widget in self.root.winfo_children():
            widget.destroy()

        tk.Label(
            self.root,
            text=f"Deck: {self.current_deck.name}",
            font=("Arial", 18, "bold")
        ).pack(pady=20)

        tk.Button(
            self.root,
            text="Add Flashcard",
            width=20,
            command=self.add_flashcard
        ).pack(pady=5)

        tk.Button(
            self.root,
            text="View Flashcards",
            width=20,
            command=self.view_flashcards
        ).pack(pady=5)

        tk.Button(
            self.root,
            text="Back",
            width=20,
            command=self.build_main_screen
        ).pack(pady=5)

    def add_flashcard(self):

        question = simpledialog.askstring(
            "Question",
            "Enter question:"
        )

        answer = simpledialog.askstring(
            "Answer",
            "Enter answer:"
        )

        if question and answer:
            self.current_deck.add_flashcard(
                question,
                answer
            )

            messagebox.showinfo(
                "Success",
                "Flashcard added."
            )

    def view_flashcards(self):

        cards = self.current_deck.get_flashcards()

        if not cards:
            messagebox.showinfo(
                "Cards",
                "No flashcards found."
            )
            return

        text = ""

        for i, card in enumerate(cards, start=1):
            text += (
                f"{i}. "
                f"{card.question} -> "
                f"{card.answer}\n"
            )

        messagebox.showinfo(
            "Flashcards",
            text
        )

    def start_quiz(self):

        if not self.current_deck:
            messagebox.showwarning(
                "Select Deck",
                "Open a deck first."
            )
            return

        if len(self.current_deck) == 0:
            messagebox.showwarning(
                "No Cards",
                "Add flashcards first."
            )
            return

        quiz = QuizManager(self.current_deck)

        cards = quiz.get_questions()

        for card in cards:

            answer = simpledialog.askstring(
                "Quiz",
                card.question
            )

            if answer is None:
                return

            quiz.check_answer(
                answer,
                card.answer
            )

        score = quiz.get_score()

        self.stats.add_score(score)

        messagebox.showinfo(
            "Quiz Complete",
            f"Score: {score}/{len(cards)}"
        )

    def show_stats(self):

        info = (
            f"Quizzes Taken: {self.stats.quizzes_taken}\n"
            f"Highest Score: {self.stats.highest_score}\n"
            f"Average Score: {self.stats.get_average()}"
        )

        messagebox.showinfo(
            "Statistics",
            info
        )

    def save_all(self):

        FileManager.save_decks(self.decks)
        self.stats.save()

        messagebox.showinfo(
            "Saved",
            "All data saved."
        )

    def exit_program(self):

        FileManager.save_decks(self.decks)
        self.stats.save()

        self.root.destroy()


if __name__ == "__main__":

    root = tk.Tk()

    app = StudyMasterGUI(root)

    root.mainloop()
