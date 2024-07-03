"""
First project name: Number Guesser game
created by: Orlando Caetano
Date: 03/07/2024
"""
import random
import time

print ("Hi! Welcome to the guessing game.")
time.sleep(3)
print ("You will need to pick a number between 1 and 100")
time.sleep(2)

guess = int(input("What is your guess?: "))
correct_number = random.randint(1,100)
guess_count = 1


while guess != correct_number:
    guess_count += 1
    if guess < correct_number:
        guess = int(input("Wrong. You need to guess higher. What is your guess?: "))
    else:
        guess = int(input("Wrong. You need to guess lower. What is your guess?: "))

print (f"Congrats! The right answer was {correct_number}. it took you {guess_count} guesses.")
