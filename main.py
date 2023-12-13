import tkinter as tk
from tkinter import messagebox
import random

class NumberGuessingGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Number Guessing Game")

        self.label = tk.Label(master, text="Enter any number:")
        self.label.pack()

        self.entry = tk.Entry(master)
        self.entry.pack()

        self.button = tk.Button(master, text="Submit", command=self.check_guess)
        self.button.pack()

        self.initialize_game()

    def initialize_game(self):
        self.target_number = random.randrange(1, 10)
        self.guesses_left = 3

    def check_guess(self):
        user_guess = self.get_user_guess()

        if user_guess is not None:
            if user_guess < self.target_number:
                self.display_message("Too low!")
            elif user_guess > self.target_number:
                self.display_message("Too high!")
            else:
                self.display_message("You guessed it right!!")
                self.initialize_game()
            self.update_guesses_left()

    def get_user_guess(self):
        try:
            guess = int(self.entry.get())
            return guess
        except ValueError:
            self.display_message("Invalid input. Please enter a valid number.")
            return None

    def update_guesses_left(self):
        self.guesses_left -= 1
        if self.guesses_left == 0:
            self.display_message(f"Out of guesses! The correct number was {self.target_number}.")
            self.initialize_game()

    def display_message(self, message):
        messagebox.showinfo("Result", message)

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("200x100")
    app = NumberGuessingGame(root)
    root.mainloop()
