#!usr/bin/env python3

import csv
import time

# Get the list of unique devil fruit classes from the data
devil_fruit_classes = set()

with open("onepiecefruits.txt", "r") as comicfile:
    comiclist = csv.reader(comicfile, delimiter=',')
    next(comiclist)  # Skip the header row
    for row in comiclist:
        fruit_class = row[2]
        devil_fruit_classes.add(fruit_class.lower())  # Store lowercase class names

# Display the available devil fruit classes to the user
print("Available devil fruit classes:")
for fruit_class in devil_fruit_classes:
    print(fruit_class)

while True:
    # Read the devil fruit class from the user
    devil_fruit_class = input("Enter the devil fruit class you want to know about: ").lower()
    if devil_fruit_class in devil_fruit_classes:
        print("Loading...")
        time.sleep(3)  # Sleep for 3 seconds to simulate loading
        break
    else:
        print("Invalid class. Please try again.")

logia_count = 0
logia_characters = []

with open("onepiecefruits.txt", "r") as comicfile:
    comiclist = csv.reader(comicfile, delimiter=',')
    next(comiclist)  # Skip the header row
    for row in comiclist:
        fruit_class = row[2].lower()  # Compare lowercase class names
        character_in_show = row[0]
        if fruit_class == devil_fruit_class:
            logia_count += 1
            logia_characters.append(character_in_show)

print(f"Number of devil fruits with {devil_fruit_class} class type: {logia_count}")
print(f"The characters with the {devil_fruit_class} type devil fruit are:")
for character_in_show in logia_characters:
    print(character_in_show)

while True:
    chosen_character = input("Which of these characters do you want to see? ")
    if chosen_character.lower() in [character.lower() for character in logia_characters]:
        print("Loading...")
        time.sleep(3)  # Sleep for 3 seconds to simulate loading
        break
    else:
        print("Invalid character. Please try again.")

if chosen_character.lower() == "monkey d. luffy":
    with open("luffy_pic.txt", "r") as file:
        luffy_pic_data = file.read()
        print(luffy_pic_data)
else:
    print("Sorry, no picture file loaded yet for this character.")

input("Press Enter to exit...")

