#!/usr/bin/env python3

# This will read the raw data on one piece fruits
# Tell me how many devil fruits have a logia type class
# Give me a list of names of characters who have logia class
import csv
# using to count the logia type class found in file
logia_count = 0
# keep a list of all the characters with a logia class
logia_characters = []
# Read the onepiece.txt file as comicfile
with open("onepiecefruits.txt", "r") as comicfile:
    ## reader() creates a list by reading target which is comicfile
    # Creates new list for each line of the file
    # delimiter is here is using the , to seperate each list
    comiclist = csv.reader(comicfile, delimiter =',')
    # Go over every row in comiclist
    for row in comiclist:
        # This is where class types are found in the list
        #     0          1        2       3        4      5
        # Character,Devil Fruit,Class,Subclass,Awakened,Status
        logia_type = row[2] 
        character_in_show = row[0]
        # Counting for logia 
        if logia_type == "Logia":
            logia_count += 1
            # listing each logia character and add to the list
            character_in_show = row[0] 
            logia_characters.append(character_in_show)
# Will be printing my findindings 
print(f"Number of devil fruits with Logia class type are, {logia_count}, total") 
print("The characters with the logia trpe devil fruit are:") 
# List the characters in a clean manner
for character_in_show in logia_characters:
    print(character_in_show)
