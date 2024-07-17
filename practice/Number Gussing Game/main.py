import random
from art import logo

def guess_number():
    return int(input("Make a guess: "))

def check_guess_number(guess_number, answer, turns):
    if guess_number == answer:
        print("You Win!")
    elif guess_number > answer:
        print("Too High")
        return turns-1
    elif guess_number < answer:
        print("Too Low")
        return turns-1

def set_difficulty():
    diff = input("Choose a difficulty. Type'easy' or 'hard' :")
    if diff == "hard":
        return HARD_LEVEL
    elif diff == "easy":
        return EASY_LEVEL

EASY_LEVEL = 10
HARD_LEVEL = 5

def game():
    print(logo)
    print("Welcome to the Number Gussing Game")
    
    is_game_end = False
    while not is_game_end:
        print("I'm thinking of a number between 1 and 100")
        answer = random.randint(1,100)
        turns = set_difficulty()
        guess = 0
        while guess != answer:
            print(f"You have {turns} attempts remaining to guess the number.")
            guess = guess_number()
            turns = check_guess_number(guess, answer, turns)
            if guess != answer:
                print("Guess again.")
            if turns == 0:
                print("You've run out of guesses, you lose.")
                break
        
        is_game_end = input("Do you want to play a game? Type 'y' or 'n':") == 'y'
game()