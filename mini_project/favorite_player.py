#!/usr/bin/env python3

# Guess my favroite basketball player 

def main():
    round = 0
    
    # List on my top 10 to choose from
    top_10_players = ["LeBron James", "Michael Jordan", "Shaquille O'Neal", "Kareem Abdul-Jabbar", "Kobe Bryant", "Steph Curry", "Wilt Chamberlain", "Bill Russell", "Magic Johnson", "Dirk Nowitzki"]
    
    # This will set LeBron James as answer and negate capitalization
    number1 = top_10_players[0].lower()

    # The setup, showing the list and prompting my question
    print("I have a list of my top 10 NBA players of all time.")
    print("You will have to guess my #1 favorite player.")
    print("I will give you 3 guesses.")
    print("My top 10 list is: ")

    # Just to cleanly list players
    for player in top_10_players:
        print(player)

    # The 3 clues I will be giving
    clues = ["My first clue is they are a top 5 scorer of all time", "My second clue is they have won multiple NBA Championships", "My final clue is they have played for 20 NBA seasons"]

    while round < 3:
        print(clues[round])
        answer = input("What is your guess? ")
        answer = answer.lower()

        if answer == number1:
            print("Congratulations! You guessed it correctly. LeBron James is my favorite player!")
            break
        else:
            print("Wrong guess. Please try again.")
            round += 1

    if round == 3:
        print("You failed to guess my favorite NBA player. The answer is LeBron James!")

    
main()
