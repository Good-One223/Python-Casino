import time
import random
import json

score = 10
betting_value = 0
bet_choice = ""
finished_horses = []
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


def get_score(begining_score):
    global score
    score = begining_score


def share_score():
    global score
    return score


def win():
    global score
    global betting_value
    global bet_choice
    global finished_horses
    if bet_choice == "r":
        bet_choice = "🔴"
    if bet_choice == "o":
        bet_choice = "🟠"
    if bet_choice == "y":
        bet_choice = "🟡"
    if bet_choice == "g":
        bet_choice = "🟢"
    if bet_choice == "b":
        bet_choice = "🔵"
    if bet_choice == "p":
        bet_choice = "🟣"
    payout = 0
    if bet_choice == finished_horses[0]:
        payout = betting_value * 10
        score += payout
        print("You won in 1st place")
        print(f"You get ${payout}, your new total is ${score}")
    elif bet_choice == finished_horses[1]:
        payout = betting_value * 5
        score += payout
        print("You won in 2nd place")
        print(f"You get ${payout}, your new total is ${score}")
    elif bet_choice == finished_horses[2]:
        payout = betting_value * 2
        score += payout
        print("You won in 3rd place")
        print(f"You get ${payout}, your new total is ${score}")
    else:
        print("Your horse was not in the top 3, you lose")
        score -= betting_value


def race():
    global score
    global betting_value
    global bet_choice
    global finished_horses
    distances = {"🔴": 80,
                 "🟠": 80,
                 "🟡": 80,
                 "🟢": 80,
                 "🔵": 80,
                 "🟣": 80,
                 }
    print(f"You have ${score}")
    betting_value = repeat_int("How much will you bet? ")
    if betting_value > score or betting_value < 0:
        print("you don't have that much money, you bet $1 instead.")
        betting_value = 1
    bet_choice = str(input(
        "Which horse will you bet on, Red(r), Orange(o), Yellow(y), Green(g), Blue(b), or Purple(p)? "))
    if bet_choice not in ("r", "o", "y", "g", "b", "p"):
        print("That's not one of the horses, you bet on a random one instead")
        bet_choice = "r" or "o" or "y" or "g" or "b" or "p"
    finished_horses = []
    print("\n" * 6)
    while len(finished_horses) < 3:
        print("\033[F" * 6, end="")
        for e, d in distances.items():
            print(f"{" " * int(d)}🐎{e}\033[K")
            if e in finished_horses:
                continue
            if d <= 0:
                finished_horses.append(e)
            distances[e] -= random.uniform(0.5, 2.5)
        time.sleep(0.1)
    print(f"\n1st: 🐎{finished_horses[0]}")
    print(f"2nd: 🐎{finished_horses[1]}")
    print(f"3rd: 🐎{finished_horses[2]}")
    win()


def play():
    global score
    while True:
        race()
        save()
        if score <= 0:
            time.sleep(2)
            return
        ret = input("Will you return to the menu, yes(y) or no(n)? ")
        if ret in ("y", "Y"):
            print("Returning to menu")
            time.sleep(2)
            return
