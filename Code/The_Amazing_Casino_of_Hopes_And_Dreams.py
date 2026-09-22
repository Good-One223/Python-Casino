import Blackjack
import Roulette
import Slot_machine
import Crash
import Horse_Race
import Poker
import json
import time

score = 0
loan_count = 0
current_loan_repayment_value = 0

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


def loan():
    global score
    global loan_count
    global current_loan_repayment_value
    if score <= 0:
        print("")
        print("You're out of money, you must take a loan.")
        print("Loans cost two times their value to pay back")
        print("and an extra two times their value for every loan you take.")
        print("The maximum loan you can take is $10000")
        print(f"You've taken out {loan_count} loans")
        loan_amount = int(input("How much will you take for a loan? "))
        if loan_amount > 10000:
            print("That is more then the maximum loan value, you take $10000 instead")
            loan_amount = 10000
        loan_cost = (loan_amount * (2 + loan_count + loan_count)
                     ) + current_loan_repayment_value
        print(f"it will take ${loan_cost} to repay your loan")
        time.sleep(2)
        print("")
        loan_count += 1
        score += loan_amount
        current_loan_repayment_value = loan_cost
        save()
        menu()


def menu():
    global score
    global current_loan_repayment_value

    if score <= 0:
        loan()

    print("Welcome to The Amazing Casino of Hopes And Dreams")
    print(f"your current balance is ${score}")
    if current_loan_repayment_value > 0:
        gorl = input("will you play a game(g) or repay your loan(l)? ")
        if gorl in ("l", "L"):
            loan_repayment_value = int(
                input(f"You owe ${current_loan_repayment_value}, you have ${score}, how much of your loan will you repay? "))
            if loan_repayment_value > score:
                print("You don't have that much money")
            elif loan_repayment_value == score:
                print("That's all your money, don't do that")
            else:
                score -= loan_repayment_value
                current_loan_repayment_value -= loan_repayment_value
                print(
                    f"you repayed ${loan_repayment_value}, you now owe ${current_loan_repayment_value}, you now have ${score}")
                save()
        else:
            pass
    current_game = input(
        "What shall you play today: Blackjack, Poker, Roulette, Slots, Crash, or Horse Race: ")

    if current_game in ("Blackjack", "blackjack", "b", "bj", "1"):
        print("")
        Blackjack.get_score(score)
        Blackjack.play()
        score = Blackjack.share_score()
        current_game = ""
        save()

    if current_game in ("Roulette", "roulette", "r", "R", "3"):
        print("")
        Roulette.get_score(score)
        Roulette.play()
        score = Roulette.share_score()
        current_game = ""
        save()

    if current_game in ("slots", "slot", "slot machine", "s", "sm", "4"):
        print("")
        Slot_machine.get_score(score)
        Slot_machine.play()
        score = Slot_machine.share_score()
        current_game = ""
        save()

    if current_game in ("crash", "Crash", "C", "c", "5"):
        print("")
        Crash.get_score(score)
        Crash.play()
        score = Crash.share_score()
        current_game = ""
        save()

    if current_game in ("horse race", "horse", "h", "H", "hr", "6"):
        print("")
        Horse_Race.get_score(score)
        Horse_Race.play()
        score = Horse_Race.share_score()
        current_game = ""
        save()

    if current_game in ("poker", "Poker", "p", "P", "5 card", "2"):
        print("")
        Poker.get_score(score)
        Poker.play()
        score = Poker.share_score()
        current_game = ""
        save()


while True:
    menu()
