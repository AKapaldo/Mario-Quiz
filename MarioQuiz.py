"""
Author: Andrew Kapaldo
Date: October 6, 2020
Version: 2.0
Python 3.8
"""

# Set Global Variables
replay = True
colorStart = '\x1b[6;30;42m'
colorEnd = '\x1b[0m'
while replay:
    score = 0
    again = "Invalid input. Enter a choice A, B, C, or D."
# Questions and Answers
    qAndA = ["\n\nHow did Mario get his name?\n A. After the US Warehouse Landlord\n B. After a Developer's Son"
             "\n C. After the Company Owner's Plumber\n D. After the Owner's Favorite Pasta Brand",
             "\n\nThe name Luigi has a similar sound to what Japanese word?\n A. Pasta\n B. Brother\n C. Similar\n "
             "D. Green",
             "\n\nWhat size is the cartridge Super Mario Brothers was stored on?\n A. 512 kilobits\n B. 128 kilobits"
             "\n C. 64 kilobits\n D. 256 kilobits",
             "\n\nHow many copies has Super Mario Bros sold?\n A. 7.95 Million\n B. 98.60 Million\n C. 40.23 Million"
             "\n D. 1.12 Billion",
             "\n\nWhat was Mario's name in Donkey Kong?\n A. Jump Man\n B. Barrel Boy\n C. Red Runner\n D. Hop Heathen"]

# Header and Instructions
    print("##################################################")
    print("###           It's a me! Mario! Quiz           ###")
    print("##################################################")

    print("\nFor each question, select the correct answer\nby typing the letter of the answer and press enter.")

# Question 1
    valid = False
    while not valid:
        print(qAndA[0])
        Q1 = input("Answer: ").upper()
        if Q1 == "A":
            score += 1
            print("Correct!")
            valid = True
        elif Q1 == "B" or Q1 == "C" or Q1 == "D":
            print("Incorrect. Mario was named after Mario Segale - the landlord for the company's warehouse.")
            valid = True
        else:
            print(colorStart + again + colorEnd)

# Question 2
    valid = False
    while not valid:
        print(qAndA[1])
        Q2 = input("Answer: ").upper()
        if Q2 == "C":
            score += 1
            print("Correct!")
            valid = True
        elif Q2 == "A" or Q2 == "B" or Q2 == "D":
            print("Incorrect. The word Luigi has the same sound as the Japanese word for \"similar\".")
            valid = True
        else:
            print(colorStart + again + colorEnd)

# Question 3
    valid = False
    while not valid:
        print(qAndA[2])
        Q3 = input("Answer: ").upper()
        if Q3 == "D":
            score += 1
            print("Correct!")
            valid = True
        elif Q3 == "A" or Q3 == "B" or Q3 == "C":
            print("Incorrect. The cartridge was 256 kilobits or 32 kilobytes.")
            valid = True
        else:
            print(colorStart + again + colorEnd)

# Question 4
    valid = False
    while not valid:
        print(qAndA[3])
        Q4 = input("Answer: ").upper()
        if Q4 == "C":
            score += 1
            print("Correct!")
            valid = True
        elif Q4 == "A" or Q4 == "B" or Q4 == "D":
            print("Incorrect. Super Mario Bros has sold 40.23 million copies.")
            valid = True
        else:
            print(colorStart + again + colorEnd)

# Question 5
    valid = False
    while not valid:
        print(qAndA[4])
        Q5 = input("Answer: ").upper()
        if Q5 == "A":
            score += 1
            print("Correct!")
            valid = True
        elif Q5 == "B" or Q5 == "C" or Q5 == "D":
            print("Incorrect. Mario was know as Jump Man when he was introduced in Donkey Kong.")
            valid = True
        else:
            print(colorStart + again + colorEnd)

# Calculate Letter Grade
    if score == 5:
        grade = "A"
    elif score == 4:
        grade = "B"
    elif score == 3:
        grade = "D"
    else:
        grade = "F"

# Calculate Percentage Score
    percent = int(score / 5 * 100)

# Print out game results
    print("\nYou got", score, "out of 5 correct!")
    if grade == "B":
        print("That is an", percent, "%", grade)
    else:
        print("That is a", percent, "%", grade)

# Ask to play again
    valid = False
    while not valid:
        playAgain = input("\nWant to play again? (y or n): ").upper()
        if playAgain == "Y" or playAgain == "YES":
            valid = True
            print("Restarting Quiz!\n\n")
        elif playAgain == "N" or playAgain == "NO":
            replay = False
            valid = True
            print("\nThanks for playing!")
        else:
            print(colorStart + "Unrecognized input." + colorEnd)
