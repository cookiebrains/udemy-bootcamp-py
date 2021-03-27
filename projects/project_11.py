import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def deal_n_cards(n):
    hand = []
    for i in range(n):
        card_index = random.randint(0, 12)
        hand.append(cards[card_index])
    return hand


def hand_value(hand):
    aces = list(filter(lambda x: x == 11, hand))
    not_aces = list(filter(lambda x: x != 11, hand))

    total = sum(aces) + sum(not_aces)

    if total > 21 and len(aces) > 0:
        for _ in aces:
            total -= 10
            if total <= 21:
                break

    return total


def add_one_card(hand):
    card_index = random.randint(0, 12)
    hand.append(cards[card_index])
    return hand


def finish_computer_hand(hand):
    while hand_value(hand) < 17:
        add_one_card(hand)
    return hand


def taking_cards(hand):
    while True:
        another_card = input("Type 'y' to get another card, type 'n' to pass: ")
        if another_card == 'y':
            hand = add_one_card(hand)
            current_hand_value = hand_value(hand)
            print(f'Your cards: {hand}, current score: {hand_value(hand)}')
            if current_hand_value > 21:
                break
        elif another_card == 'n':
            print(f'Your final hand: {hand}, final score {hand_value(hand)}')
            break
    return hand


def declare_winner(player_hand, computer_hand):
    if hand_value(player_hand) > 21:
        print("You bust. You lose.")
    elif hand_value(player_hand) < 22 and hand_value(computer_hand) < 22:
        if hand_value(player_hand) > hand_value(computer_hand):
            print("You win!")
        elif hand_value(player_hand) < hand_value(computer_hand):
            print("You lose.")
    elif hand_value(computer_hand) > 21 and hand_value(player_hand) < 22:
        print("Computer busts. You win!")
    elif hand_value(computer_hand) == hand_value(player_hand):
        print("Draw!")


def game():
    player_hand = deal_n_cards(2)
    computer_hand = deal_n_cards(1)
    print(f'Your cards: {player_hand}, current score: {hand_value(player_hand)}')
    print(f"Computer's first card: {computer_hand}")
    final_player_hand = taking_cards(player_hand)
    final_computer_hand = finish_computer_hand(computer_hand)
    print(f"Computer's final hand: {final_computer_hand}, final score: {hand_value(final_computer_hand)}")
    declare_winner(final_player_hand, final_computer_hand)


def run():
    while True:
        game()
        choose_to_cont = input(f"Do you want to play another game of Blackjack? Type 'y' or 'n':")
        if choose_to_cont == 'n':
            break
    print('Thanks for playing!')
