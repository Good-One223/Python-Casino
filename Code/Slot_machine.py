import time
import random
import json

score = 1
rig = 15
icons = ["🍎", "🍇", "🍉", "🍒", "🍫", "💎", "💰"]
chance = [20, 15, 15, 15, 10, 20, 5]
multi = [10, 20, 20, 30, 50, 20, 150]
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


def display(i1, i2, i3):
    count = 0
    v1 = random.randint(150, 250)
    v2 = random.randint(350, 450)
    v3 = random.randint(550, 700)
    while True:
        if count < v1:
            display1 = random.choices(icons)[0]
        else:
            display1 = i1
        if count < v2:
            display2 = random.choices(icons)[0]
        else:
            display2 = i2
        if count < v3:
            display3 = random.choices(icons)[0]
        else:
            display3 = i3
        print(f"\r{display1} {display2} {display3}", end="")
        if count == 700:
            break
        count += 1
        time.sleep(0.01)


def pick_icons():
    global score
    global betting_value
    global rig
    icon1 = random.choices(icons, weights=chance, k=1)[0]
    increased_odds = chance.copy()
    lucky_symbol = icons.index(icon1)
    increased_odds[lucky_symbol] += rig
    icon2 = random.choices(icons, weights=increased_odds, k=1)[0]
    icon3 = random.choices(icons, weights=increased_odds, k=1)[0]

    display(icon1, icon2, icon3)

    if icon1 == icon2 == icon3:
        winning_symbol = icons.index(icon1)
        money_won = betting_value * multi[winning_symbol]
        score += money_won
        rig -= 20
        print(
            f"\nCongratulations, you won ${money_won}, you now have ${score}")
    elif (icon1 == "💎" and icon2 == "💎" and icon3 != "💎") or (icon1 == "💎" and icon3 == "💎" and icon2 != "💎") or (icon2 == "💎" and icon3 == "💎" and icon1 != "💎"):
        score += betting_value
        print(
            f"\ndouble diamonds, you win ${betting_value}, you now have ${score}")
    elif icon1 == "💎" or icon2 == "💎" or icon3 == "💎":
        print(
            f"\nYou lost, but you got a diamond, you don't lose anything, you have ${score}")
    elif icon1 != icon2 or icon1 != icon3 or icon2 != icon3:
        score -= betting_value
        rig += 5
        print(f"\nYou lost ${betting_value}, you now have ${score}")


def play():
    global betting_value
    global rig
    betting_value = repeat_int(
        f"You're starting with ${score}, how much do you want to bet each spin: ")
    while True:
        new_betting_value = input(
            "If you want to change your bet amount type it, else press enter: ")
        if new_betting_value.strip() != "":
            betting_value = int(new_betting_value)
        if betting_value < 0:
            betting_value = 0
        pick_icons()
        save()
        time.sleep(1)
        if score <= 0:
            print("You're out of money, you lose")
            print("This is why you should never gamble")
            time.sleep(4)
            print("Because you're bad at it")
            time.sleep(2)
            break
        ret = input("Will you return to the menu, yes(y) or no(n)? ")
        if rig <= 0:
            rig = 5
        if ret in ("y", "Y", " y"):
            print("Returning to menu")
            time.sleep(2)
            return
