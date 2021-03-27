import random

num = random.randint(1, 100)


def guess_the_number(mode):
    times = 1
    if mode == 'easy':
        times = 10
    if mode == 'hard':
        times = 5
    guess = 0
    while guess != num:
        print(f'You have {times} attempts remaining to guess the number. ')
        guess = int(input('Make a guess: '))
        if guess < num:
            print('Too low!')
        if guess > num:
            print('Too high!')
        times -= 1
        if times == 0:
            break
    if guess == num:
        print(f'You got it! The number was {num}!')
    else:
        print('You lose! The number was ', num)


def game():
    print("Welcome to the Number Guessing Game!/n I'm thinking of a number between 1 and 100.")
    mode = input("Choose a difficulty. Type 'easy' or 'hard': ")
    guess_the_number(mode)


def run():
    game()
