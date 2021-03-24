import random

word_list = ["aardvark", "baboon", "camel"]

# TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

# TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

# TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

chosen_word = random.choice(word_list)

display = []
for letter in chosen_word:
    display.append('_')


def run():
    print(display)
    guess = input('Guess a letter:')
    for letter in chosen_word:
        if letter == guess:
            display[chosen_word.] = letter
        else:
            print("NO")
    print(chosen_word)
