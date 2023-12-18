# NUMBER GUESSING GAME
import random
import tkinter as tk
from tkinter import messagebox

computer_guess = random.randint(0, 9)


# Functions
# reset
def reset():
    global computer_guess
    computer_guess = random.randint(0, 9)
    guider_label["text"] = "New number"
    number_entry.delete(0, "end")


# check
def check():
    user_guess = number_entry.get()
    try:
        user_guess = int(user_guess)
        if user_guess == computer_guess:
            guider_label["text"] = "Correct"
        elif user_guess < computer_guess:
            guider_label["text"] = "Higher"
        elif user_guess > computer_guess:
            guider_label["text"] = "Lower"
    except:
        tk.messagebox.showerror("Error", "You must enter a number")

    number_entry.delete(0, "end")


# create window application
window = tk.Tk()
window.title("Number Guessing Game")
window.geometry("300x110")

# Labels
guider_label = tk.Label(window, text="Guess!", font=50, padx=10, pady=10, width=10)
guider_label.grid(row=0, column=1)

# Buttons
# check button
check_button = tk.Button(window, text="Check", font=40, command=check)
check_button.grid(row=1, column=0, padx=5, pady=10)
# reset button
reset_button = tk.Button(window, text="Reset", font=40, command=reset)
reset_button.grid(row=1, column=2, padx=5, pady=10)

# Entry
number_entry = tk.Entry(window, font=40, width=5)
number_entry.grid(row=1, column=1)

# main loop
window.mainloop()
