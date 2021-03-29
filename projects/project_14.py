from input_files import data, hl_logo, vs
import random


def select_two_candidates():
    """Returns a list of two randomly selected candidates
    """
    candidates = []
    for _ in range(2):
        num = random.randint(0, 49)
        candidates.append(data[num])
    return candidates


def string_from_dict(candidate):
    name = candidate['name']
    description = candidate['description']
    location = candidate['country']
    return f'{name}, a {description} from {location}'


def present_choices(candidates):
    candidate_a = candidates[0]
    candidate_b = candidates[1]
    print(f'Compare A: {string_from_dict(candidate_a)}')
    print(vs)
    print(f'Against B: {string_from_dict(candidate_b)}')


def is_correct(candidates, choice):
    candidate_a = candidates[0]
    candidate_b = candidates[1]
    count_a = candidate_a["follower_count"]
    count_b = candidate_b["follower_count"]
    if count_a > count_b and choice == 'b':
        return True
    elif count_b > count_a and choice == 'a':
        return True
    else:
        return False


def game():
    print(hl_logo)
    score = 0
    while True:
        candidates = select_two_candidates()
        present_choices(candidates)
        choice = input("Who has more followers? Type 'A' or 'B': ").lower()
        if is_correct(candidates, choice):
            score += 1
            print(f"You're right! Current Score: {score}\n\n")
        else:
            print(f"Sorry, that's wrong. Final score: {score}")
            break


def run():
    game()
