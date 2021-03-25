import random
from input_files import word_list

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

chosen_word = random.choice(word_list)
word_length = len(chosen_word)


def run():
    lives = 6
    # Testing code
    print(f'Welcome to Hangman')
    end_of_game = False
    display = []

    # Create blanks
    for letter in range(word_length):
        display.append('_')
    print(display)
    while not end_of_game:
        guess = input('Guess a letter: ').lower()

        if guess in display:
            print(f"You've already guessed {guess}")

        # check guessed letter
        for position in range(word_length):
            letter = chosen_word[position]

            if letter == guess:
                display[position] = letter

        if guess not in chosen_word:
            print(f"You've guessed {guess}, that's not in the word. You are one step closer to hanging.")
            lives -= 1

        print(f"{''.join(display)}")
        if "_" not in display:
            end_of_game = True
            print("You Win!!")
        if lives == 0:
            end_of_game = True
            print("You Lose")
            print(f'The word was {chosen_word}')

        print(stages[lives])
