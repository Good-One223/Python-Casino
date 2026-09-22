from random import shuffle
import time
from collections import Counter
import json

score = 10
betting_value = 0
hand_type = ""
dealer_hand_type = ""

suits = ["♣", "♥", "♦", "♠"]
values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
deck = []
dealer_cards = []
player_cards = []

file_name = "TheAmazingCasinoOfHopesAndDreams.json"

try:
    with open(file_name, "r") as file:
        save_data = json.load(file)
        score = save_data["score"]
        loan_count = save_data["loan_count"]
        current_loan_repayment_value = save_data["current_loan_repayment_value"]
except FileNotFoundError:
    score = 1000
    loan_count = 0
    current_loan_repayment_value = 0


def get_score(begining_score):
    global score
    score = begining_score


def share_score():
    global score
    return score


def save():
    save_data = {
        "score": score,
        "loan_count": loan_count,
        "current_loan_repayment_value": current_loan_repayment_value
    }
    with open(file_name, "w") as file:
        json.dump(save_data, file, indent=4)


def repeat_int(question):
    while True:
        try:
            return int(input(question))
        except ValueError:
            print("Please use a whole number with no aditional characters.")


def hand(cards_to_check):
    val_map = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7,
               "8": 8, "9": 9, "10": 10, "J": 11, "Q": 12, "K": 13, "A": 14}
    card_values = sorted([val_map[card[:-1]] for card in cards_to_check])
    card_suits = [card[-1] for card in cards_to_check]
    is_flush = len(set(card_suits)) == 1
    is_normal_straight = (len(set(card_values)) ==
                          5 and card_values[-1] - card_values[0] == 4)
    is_wheel_straight = (card_values == [2, 3, 4, 5, 14])
    is_straight = is_normal_straight or is_wheel_straight
    value_counts = list(Counter(card_values).values())
    if is_flush and is_straight:
        if card_values[-1] == 14 and not is_wheel_straight:
            return "Royal Flush"
        return "Straight Flush"
    elif 4 in value_counts:
        return "Four of a Kind"
    elif 3 in value_counts and 2 in value_counts:
        return "Full House"
    elif is_flush:
        return "Flush"
    elif is_straight:
        return "Straight"
    elif 3 in value_counts:
        return "Three of a Kind"
    elif value_counts.count(2) == 2:
        return "Two Pair"
    elif 2 in value_counts:
        return "Pair"
    else:
        return "High Card"


def deal(noc, target_hand):
    global deck
    for i in range(noc):
        if deck:
            target_hand.append(deck.pop(0))
            shuffle(deck)


def discard_and_play():
    global score
    global player_cards
    global dealer_cards
    global hand_type
    global dealer_hand_type
    global betting_value
    i = 0
    print("You can now discard up to 10 cards\nto select a card type its position number (1-5)")
    print('For example to discard the 2nd card type "2" once finished discarding, press Enter.')
    while i < 10:
        print(f"Your cards: {' '.join(player_cards)}")
        discard = input("What Card position will you discard: ")
        if discard in ("1", "2", "3", "4", "5"):
            discard = int(discard) - 1
            if discard < len(player_cards):
                player_cards.pop(discard)
                deal(1, player_cards)
                i += 1
            else:
                print("nuh uh")
        elif discard == "":
            break
        else:
            print("That's not one of the card placements")

    print("You are playing the cards:")
    print(" ".join(player_cards))
    time.sleep(2)
    hand_type = hand(player_cards)
    print(f"You're playing a {hand_type}")
    dealer_values = [card[:-1] for card in dealer_cards]
    counts = Counter(dealer_values)
    dealer_discard_indices = []
    for index, card in enumerate(dealer_cards):
        val = card[:-1]
        if counts[val] == 1 and len(dealer_discard_indices) < 3:
            dealer_discard_indices.append(index)
    for index in sorted(dealer_discard_indices, reverse=True):
        dealer_cards.pop(index)
    deal(5 - len(dealer_cards), dealer_cards)
    dealer_hand_type = hand(dealer_cards)
    print(f"Dealer's Hand: {' '.join(dealer_cards)}")
    print(f"Dealer played a {dealer_hand_type}")
    hand_ranks = [
        "Royal Flush", "Straight Flush", "Four of a Kind", "Full House",
        "Flush", "Straight", "Three of a Kind", "Two Pair", "Pair", "High Card"
    ]
    p_score = hand_ranks.index(hand_type)
    d_score = hand_ranks.index(dealer_hand_type)
    if p_score < d_score:
        winnings = betting_value * (d_score - p_score) * 3
        print(
            f"You win, you got ${winnings}")
        score += winnings
    elif p_score > d_score:
        print(f"Dealer wins you lost ${betting_value}")
        score -= betting_value
    else:
        print("It's a tie!")


def betting():
    global betting_value
    global score
    global player_cards
    global dealer_cards
    global deck
    player_cards = []
    dealer_cards = []
    deck = [f"{value}{suit}" for value in values for suit in suits]
    shuffle(deck)
    betting_value = repeat_int(f"You have ${score}, how much will you bet? ")
    if betting_value < 0 or betting_value > score:
        print("You don't have that much money, you bet $1 instead.")
        betting_value = 1
    deal(5, player_cards)
    deal(5, dealer_cards)
    discard_and_play()


def play():
    while True:
        betting()
        save()
        if score <= 0:
            print("You're out of money, you lose")
            time.sleep(3)
            break
        ret = input("Will you return to the menu, yes(y) or no(n)? ")
        if ret in ("y", "Y"):
            print("Returning to menu")
            time.sleep(2)
            return
