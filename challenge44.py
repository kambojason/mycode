#!/usr/bin/env python3

def main():
    num = int(input("Choose number of bottles of beer on the wall to start with: "))
    if num > 100:
        print("Cannot start at more than 100")
        return

    for x in range(num, 0, -1):
        print(f"{x} bottles of beer on the wall! {x} bottles of beer! Take one down, pass it around,")
        print(f"{x-1} bottles of beer on the wall!")
    
     x = 1
        print(f"{x} bottle of beer on the wall! {x} bottle of beer! Take one down, pass it around,")
        print("No more bottles of beer on the wall!")





main()

