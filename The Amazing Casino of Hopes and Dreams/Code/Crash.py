import time
import random
import math
import keyboard
import json

score = 10
betting_value = 0
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


def get_score(begining_score):
    global score
    score = begining_score


def share_score():
    global score
    return score


def repeat_int(question):
    while True:
        try:
            return int(input(question))
        except ValueError:
            print("Please use a whole number with no aditional characters.")


def multi():
    global score
    global betting_value
    betting_value = repeat_int(f"You have ${score}, how much will you bet? ")
    if betting_value < 0 or betting_value > score:
        print("Not today sucker, you bet $1 instead")
        betting_value = 1
    print("Press space at any time to cash out, cash out before it crashes")
    low = 0.1
    high = 10.0
    curve = random.betavariate(alpha=1.66, beta=3.65)
    last_multi = round(low + (high - low) * curve, 2)
    current_multi = low
    total_change = math.ceil((last_multi - low) * 100)
    kept_multi = 0.00
    cash_out = False
    for i in range(total_change):
        if keyboard.is_pressed("space"):
            keyboard.send("backspace")
            cash_out = True
            kept_multi = round(current_multi, 2)
            break
        current_payout = betting_value * current_multi
        print(
            f"\rMultiplier: {current_multi:.2f}x  Potential Payout: ${current_payout:.2f}  ", end="")
        current_multi += 0.01
        time.sleep(0.1)
    if cash_out:
        payout = betting_value * kept_multi
        score += payout
        payout = int(payout)
        score = int(score)
        print(f"\nYou win")
        print(f"You got ${payout}, your new total is ${score}")
    else:
        score -= betting_value
        print(f"\nyou lose")
        print(f"You lost ${betting_value}, your new total is ${score}")


def play():
    global score
    print("Welcome to Crash")
    while True:
        multi()
        save()
        if score <= 0:
            print("You're out of money, you lose")
            time.sleep(2)
            break
        ret = input("Will you return to the menu, yes(y) or no(n)? ")
        if ret in ("y", "Y"):
            print("Returning to menu")
            time.sleep(2)
            return
        print("\n")
