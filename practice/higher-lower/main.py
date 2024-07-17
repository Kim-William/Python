
from art import vs, logo
from game_data import data
import random
import os

# format Data
def format_data(account):
    name = account["name"]
    description = account["description"]
    country = account["country"]
    return f"{name}, a {description}, {country}"

# Display A vs B
def DisplayAvsB(account_a, account_b):
    print(f"Compare A: {format_data(account_a)}")
    print(vs)
    print(f"Against B: {format_data(account_b)}")

# Select A ot B
def select_follower():
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    return guess

# Compare A and B
def compare_A_and_B(account_a, account_b):
    if  account_a["follower_count"] > account_b["follower_count"]:
        return "a"
    else:
        return "b"

# Get Random value for B
def get_random_value():
    return random.choice(data)

def game():
    print(logo)

    game_should_continue = True
    score = 0
    account_a = get_random_value()
    account_b = get_random_value()

    while game_should_continue:
        account_a = account_b
        account_b = get_random_value()

        while account_a == account_b:
            account_b = get_random_value()
        DisplayAvsB(account_a, account_b)
        
        guess = select_follower()
        answer = compare_A_and_B(account_a, account_b)

        os.system("cls")
        print(logo)
        if guess == answer:
            score+=1
            print(f"You're right! Current scoure: {score}")
        else:
            game_should_continue = False
            print(f"Sorry, that's wrong. Final score: {score}")

game()



# Shift B to A


# Calculate Score

