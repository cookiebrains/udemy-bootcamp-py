# Caesar Cipher
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']


#  A function called 'encrypt' that takes the 'text' and 'shift' as inputs.

def caesar(direction, text, shift):
    output_text = ''
    if direction == 'decode':
        shift *= -1

    for char in text:
        if char not in alphabet:
            output_text += char
        else:
            starting_index = alphabet.index(char)
            shift_index = (starting_index + shift) % 26
            output_text += alphabet[shift_index]

    print(f'The {direction}d text is: {output_text}')


def encrypt(to_encode, shift):
    encrypted_text = ''
    for letter in to_encode:
        starting_index = alphabet.index(letter)
        if starting_index + shift < 26:
            shift_index = starting_index + shift
        else:
            shift_index = (starting_index + shift) - 26
        encrypted_text += alphabet[shift_index]

    print(f'The encoded text is {encrypted_text}.')


def decrpyt(to_decode, shift):
    decrypted_text = ''
    for letter in to_decode:
        starting_index = alphabet.index(letter)
        shift_index = starting_index - shift
        decrypted_text += alphabet[shift_index]

    print(f'The decoded text is {decrypted_text}.')


def run():
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(direction, text, shift)
    run_again = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if run_again == 'yes':
        run()
    if run_again == 'no':
        print('Goodbye')
        quit()
