import random
import time
import json

score = int(1)
winning_number = 0
bet_value = int(0)
bet_type = str("")
single_value = int(0)
dozens_type = str("")

Red_numbers = (1, 3, 5, 7, 9, 12, 14, 16, 18, 19,
               21, 23, 25, 27, 30, 32, 34, 36)
Black_numbers = (2, 4, 6, 8, 10, 11, 13, 15, 17,
                 20, 22, 24, 26, 28, 29, 31, 33, 35)

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


def colour(number):
    if number == 0:
        return "🟢"
    elif number in Red_numbers:
        return "🔴"
    elif number in Black_numbers:
        return "⚫"


def betting():
    global score
    global single_value
    global bet_type
    global bet_value
    global dozens_type
    bet_value = repeat_int(
        f"You have ${score}, how much will you bet this round? ")
    if bet_value < 0 or bet_value > score:
        print("you don't have that much money, you bet $0 instead")
        bet_value = 0
    bet_type = input(
        "will you bet Odd(o), Even(e), Red(r), Black(b), Low(l), high(h), single(s), dozens(d), columns(c)? ")
    if bet_type in ("s", "S"):
        single_value = repeat_int("What number are you betting on? ")
    if bet_type in ("d", "D"):
        dozens_type = input(
            "Will you bet first dozen(f), second dozen(s), or third dozen(t)? ")
    if dozens_type not in ("f", "F", "s", "S", "t", "T"):
        dozens_type = "f" or "s" or "t"
    if bet_type in ("c", "C"):
        dozens_type = input(
            "Will you bet first column(f), second column(s), or third column(t)? ")
    if dozens_type not in ("f", "F", "s", "S", "t", "T"):
        dozens_type = "f" or "s" or "t"


def winner():
    global score
    global winning_number
    global bet_value
    global bet_type
    global single_value
    global dozens_type
    money_won = 0

    if bet_type in ("o", "O"):
        if winning_number in (1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35):
            money_won = bet_value * 4
            score += money_won
            print(f"It's an odd number, you win ${money_won}")
        else:
            score -= bet_value
            print(f"It's an even number, you lose")

    if bet_type in ("e", "E"):
        if winning_number in (2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36):
            money_won = bet_value * 4
            score += money_won
            print(f"It's an even number, you win ${money_won}")
        else:
            score -= bet_value
            print("It's an odd number, you lose")

    if bet_type in ("r", "R"):
        if winning_number in (1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36):
            money_won = bet_value * 4
            score += money_won
            print(f"It's red, you win ${money_won}")
        else:
            score -= bet_value
            print(f"It's black, you lose")

    if bet_type in ("b", "B"):
        if winning_number in (2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35):
            money_won = bet_value * 4
            score += money_won
            print(f"It's black, you win ${money_won}")
        else:
            score -= bet_value
            print("It's red, you lose")

    if bet_type in ("l", "L"):
        if winning_number <= 18 and winning_number != 0:
            money_won = bet_value * 4
            score += money_won
            print(f"It's a low number, you win ${money_won}")
        else:
            score -= bet_value
            print(f"It's a high number, you lose")

    if bet_type in ("h", "H"):
        if winning_number >= 19:
            money_won = bet_value * 4
            score += money_won
            print(f"It's a high number, you win ${money_won}")
        else:
            score -= bet_value
            print("It's a low number, you lose")

    if bet_type in ("s", "S"):
        if winning_number == single_value:
            money_won = bet_value * 100
            score += money_won
            print(f"It's {single_value}, you win {money_won}")
        elif winning_number != single_value:
            score -= bet_value
            print(f"It's not {single_value}, you lose")

    if bet_type in ("d", "D"):
        if dozens_type == "f":
            if 1 <= winning_number <= 12:
                money_won = bet_value * 8
                score += money_won
                print(f"It's in the first dozen, you win ${money_won}")
            else:
                score -= bet_value
                print("It's not in the first dozen, you lose")
        elif dozens_type == "s":
            if 13 <= winning_number <= 24:
                money_won = bet_value * 8
                score += money_won
                print(f"It's in the second dozen, you win ${money_won}")
            else:
                score -= bet_value
                print("It's not in the second dozen, you lose")
        elif dozens_type == "t":
            if 25 <= winning_number <= 36:
                money_won = bet_value * 8
                score += money_won
                print(f"It's in the third dozen, you win ${money_won}")
            else:
                score -= bet_value
                print("It's not in the third dozen, you lose")

    if bet_type in ("c", "C"):
        if dozens_type == "f":
            if winning_number in (1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31, 34):
                money_won = bet_value * 8
                score += money_won
                print(f"It's in the first column, you win ${money_won}")
            else:
                score -= bet_value
                print("It's not in the first column, you lose")
        elif dozens_type == "s":
            if winning_number in (2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35):
                money_won = bet_value * 8
                score += money_won
                print(f"It's in the second column, you win ${money_won}")
            else:
                score -= bet_value
                print("It's not in the second column, you lose")
        elif dozens_type == "t":
            if winning_number in (3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36):
                money_won = bet_value * 8
                score += money_won
                print(f"It's in the third column, you win ${money_won}")
            else:
                score -= bet_value
                print("It's not in the third column, you lose")


def spin():
    global winning_number
    winning_number = random.randint(0, 36)
    total_numbers = 37
    base_spins = 600
    slowing_spins = 45
    total_spins = base_spins + slowing_spins
    start_number = (winning_number - total_spins) % total_numbers
    current_number = start_number
    time_to_sleep = 0.01
    betting()
    for i in range(total_spins):
        brg = colour(current_number)
        print(f"\r{current_number:<2} {brg} ", end="", flush=True)
        time.sleep(time_to_sleep)
        if i >= base_spins:
            time_to_sleep *= 1.0786
        current_number = (current_number + 1) % total_numbers
    winning_colour = colour(winning_number)
    print(f"\r{current_number:<3}{winning_colour} ", end="", flush=True)
    winner()


def play():
    global winning_number
    global bet_value
    global bet_type
    global single_value
    global dozens_type
    while True:
        spin()
        save()
        winning_number = 0
        bet_value = int(0)
        bet_type = str("")
        single_value = int(0)
        dozens_type = str("")
        time.sleep(2)
        if score <= 0:
            print("You're out of money, you lose")
            time.sleep(1)
            print("you should never gamble")
            time.sleep(3)
            break
        ret = input("Will you return to the menu, yes(y) or no(n)? ")
        if ret in ("y", "Y"):
            print("Returning to menu")
            time.sleep(2)
            return
