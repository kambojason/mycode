#!usr/bin/python3

# challenge 1 and 2


round = 0
answer = " "


while round < 3 and (answer != "Brian" and answer != "Shrubbery"):
    round += 1
    answer = input('Finish the movie title, "Monthy Python\'s The Life of ______": ')
    answer = answer.capitalize()

    if answer == "Brian":
        print("Correct!")
    elif answer == "Shrubbery":
        print("You gave the secret answer!")
    elif round == 3: 
        print("Sorry answer was Brian")
    else:
        print("Please try again")

