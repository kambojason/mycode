#!/usr/bin/env python3

import random

# give the computer some options to pick from
options = ["rock", "paper", "scissors"]

# let computer choose
computer_choice = random.choice(options)
print(computer_choice)

# let human choose
user_choice = input("Enter your choice (rock/paper/scissors): ").lower()
print(user_choice)

# compare choices
if user_choice == computer_choice:
    print("It's a tie!")

elif user_choice == 'rock' and computer_choice == 'scissors':
    print("Congradulations you win")

elif user_choice == 'paper' and computer_choice == 'rock':
    print("Congradulations you win!")

elif user_choice == 'scissors' and computer_choice == 'paper':
    print("Congradulations you win!")

else:
    print("Ooops! Computer wins!")

# display result
