import tkinter as tk
from tkinter import messagebox
import random

# Function to determine the winner
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "You win!"
    else:
        return "You lose!"

# Function to handle user input
def user_choice(choice):
    # Computer makes a random choice
    computer_choice = random.choice(["rock", "paper", "scissors"])
    
    # Determine the winner
    result = determine_winner(choice, computer_choice)
    
    # Update the labels
    result_label.config(text=f"Result: {result}")
    user_choice_label.config(text=f"Your Choice: {choice}")
    computer_choice_label.config(text=f"Computer's Choice: {computer_choice}")
    
    # Update scores based on the result
    global user_score, computer_score
    if result == "You win!":
        user_score += 1
    elif result == "You lose!":
        computer_score += 1
    
    # Update score labels
    user_score_label.config(text=f"Your Score: {user_score}")
    computer_score_label.config(text=f"Computer's Score: {computer_score}")
    
    # Ask if the user wants to play again
    play_again()

# Function to ask if the user wants to play again
def play_again():
    response = messagebox.askyesno("Play Again?", "Do you want to play another round?")
    if response:
        result_label.config(text="Result: ")
        user_choice_label.config(text="Your Choice: ")
        computer_choice_label.config(text="Computer's Choice: ")
    else:
        root.quit()

# Create the main window
root = tk.Tk()
root.title("Rock, Paper, Scissors Game")

# Initialize scores
user_score = 0
computer_score = 0

# Add labels for instructions
instructions_label = tk.Label(root, text="Choose rock, paper, or scissors", font=("Arial", 14))
instructions_label.pack(pady=10)

# Add buttons for user to choose
rock_button = tk.Button(root, text="Rock", width=20, command=lambda: user_choice("rock"))
rock_button.pack(pady=5)

paper_button = tk.Button(root, text="Paper", width=20, command=lambda: user_choice("paper"))
paper_button.pack(pady=5)

scissors_button = tk.Button(root, text="Scissors", width=20, command=lambda: user_choice("scissors"))
scissors_button.pack(pady=5)

# Labels to show user and computer choices and the result
user_choice_label = tk.Label(root, text="Your Choice: ", font=("Arial", 12))
user_choice_label.pack(pady=5)

computer_choice_label = tk.Label(root, text="Computer's Choice: ", font=("Arial", 12))
computer_choice_label.pack(pady=5)

result_label = tk.Label(root, text="Result: ", font=("Arial", 14))
result_label.pack(pady=10)

# Labels to show the scores
user_score_label = tk.Label(root, text=f"Your Score: {user_score}", font=("Arial", 12))
user_score_label.pack(pady=5)

computer_score_label = tk.Label(root, text=f"Computer's Score: {computer_score}", font=("Arial", 12))
computer_score_label.pack(pady=5)

# Run the main loop
root.mainloop()