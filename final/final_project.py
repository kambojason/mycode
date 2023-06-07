#!usr/bin/env python3
"""My final Python Project"""
from crayons import green, red, blue, yellow, magenta, cyan
import csv
import time
# Game description for the users
print(magenta("One Piece is a popular anime, the characters in this show gain special powers from consuming what they refer to as devil fruit. In this program I will display the different classes for you to select to see which characters have the choosen devil fruit class."))
# Get the list of unique devil fruit classes from the data
devil_fruit_classes = set()
# This will read the txt file and arrange the data to be used in the code
# This is where class types are found in the list
#     0          1        2       3        4      5
# Character,Devil Fruit,Class,Subclass,Awakened,Status
with open("onepiecefruits.txt", "r") as comicfile:
    comiclist = csv.reader(comicfile, delimiter=',')
    next(comiclist)  # Skip the header row
    for row in comiclist:
        fruit_class = row[2]
        devil_fruit_classes.add(fruit_class.lower())  # Store lowercase class names
# Display the available devil fruit classes to the user
print(blue("\nAvailable devil fruit classes:"))
for fruit_class in devil_fruit_classes:
    print(blue(fruit_class))
while True:
    # Read the devil fruit class the user inputed and in lower case
    devil_fruit_class = input(green("\nEnter the devil fruit class you want to see the list of characters for: ")).lower()
    if devil_fruit_class in devil_fruit_classes:
        print("\nLoading...")
        time.sleep(3)  # Sleep for 3 seconds to simulate loading
        break
    else:
        print(yellow("\nInvalid class. Please try again."))
# keep count of the amount of characters with picked class
class_count = 0
class_characters = []
with open("onepiecefruits.txt", "r") as comicfile:
    comiclist = csv.reader(comicfile, delimiter=',')
    next(comiclist)  # Skip the header row
    for row in comiclist:
        fruit_class = row[2].lower()  # Compare lowercase class names
        character_in_show = row[0]
        if fruit_class == devil_fruit_class:
            class_count += 1
            class_characters.append(character_in_show)
# print my results for character names and count 
print(blue(f"\nNumber of devil fruits with {devil_fruit_class} class type: {class_count}"))
print(blue(f"The characters with the {devil_fruit_class} type devil fruit are:"))
print("\nLoading...")
time.sleep(7)
for character_in_show in class_characters:
    print(blue(character_in_show))
while True:
    chosen_character = input(green("\nWhich of these characters do you want to see? "))
    if chosen_character.lower() in [character.lower() for character in class_characters]:
        print("\nLoading...")
        time.sleep(3)  # Sleep for 3 seconds to simulate loading
        break
    else:
        print(yellow("\nInvalid character. Please try again."))
# show a picture of Monkey D. Luffy from txt file I created for him
if chosen_character.lower() == "monkey d. luffy":
    with open("luffy_pic.txt", "r") as file:
        luffy_pic_data = file.read()
        print(red(luffy_pic_data))
# show a picture of Portgas D. Ace from txt file I created for him
elif chosen_character.lower() == "portgas d. ace":
    with open("ace_pic.txt", "r") as afile:
        ace_pic_data = afile.read()
        print(cyan(ace_pic_data))
else:
    print("\nSorry, no picture file loaded yet for this character.")
# Allow user to hit enter to exit code
input(green("\nPress Enter to exit..."))

