import random

x = random.randint(1,10)

def game():

    guess = int(input("Enter your guess: "))
    while guess != x:
        game()
    if guess == x:
        x = x+1
        print("Correct.")

game()