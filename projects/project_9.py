
def add_bid_info_to_dict(bidder_name, bid):
    bid = int(''.join(filter(str.isdigit, bid)))
    dict_entry = {'bidder': bidder_name, 'bid': bid}
    return dict_entry


def the_winner(list_of_bids):
    high_bid = 0
    high_bidder = ()
    for entry in list_of_bids:
        if entry['bid'] > high_bid:
            high_bid = entry['bid']
            high_bidder = entry['bidder']

    return high_bidder, high_bid


def run():
    all_bids = []
    should_continue = True
    while should_continue:
        bidder_name = input("What is your name?:\n")
        bid = input("What is your bid?:\n")
        all_bids.append(add_bid_info_to_dict(bidder_name, bid))
        run_again = input("Are there any other bidders? Type 'yes' or 'no'.\n")

        if run_again == 'no':
            should_continue = False

    winning_info = the_winner(all_bids)
    print(f'The winner is {winning_info[0]} with a bid of ${winning_info[1]}.')
