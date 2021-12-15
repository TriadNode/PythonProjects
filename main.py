#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

from art import logo
from random import randint


EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5






def difficulty():
    DIFFICULTY = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if DIFFICULTY == 'easy':
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS

def check_answer(guess, answer, turns):
    if guess > answer:
        print("Guess too high ")
        return turns - 1
    elif guess < answer:
        print("Guess too low")
        return turns - 1
    else:
        print(f"You got it! The answer was {answer}")


def game():
    print(logo)
    print("Welcome to the Number Guessing Game")
    print("I'm thinking of a number between 1 and 100.")
    answer = int(randint(0,100))
    #print (answer)
    turns = difficulty()
    
    guess = 0
    while guess != answer:
        print(f"You have {turns} guesses.")
        guess = int(input("What is your guess? "))

        turns = check_answer(guess,answer,turns)




game()