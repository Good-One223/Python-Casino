import random
import time
import json
player = 0
dealer = 0
score = 1
beting_value = 0
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


def higher_or_lower(d, p):
    global score
    global beting_value
    kill = 0
    print(f"dealer:", d, "player:", p)
    if p > 21:
        print("you bust!")
        kill += 1
        score -= beting_value
    if d > 21:
        print("Dealer bust, you win!")
        score += beting_value
        kill += 1
    elif d > p and kill == 0:
        print("dealer wins!")
        score -= beting_value
    elif p > d and kill == 0:
        score += beting_value
        print("you win!")
    elif p == d or d > 21 and p > 21:
        print("it's a tie, flip a coin")
        dht = random.randint(1, 2)
        ht = input('type "h" or "t": ')
        if ht in ("h", "H") and dht == 1:
            score += beting_value
            print("it's heads, you win!")
        if ht in ("t", "T") and dht == 1:
            print("it's heads, you lose")
            score -= beting_value
        if ht in ("h" or "H") and dht == 2:
            print("it's tails, you lose")
            score -= beting_value
        if ht in ("t" or "T") and dht == 2:
            score += beting_value
            print("it's tails, you win!")


def draw():
    global player
    global dealer
    global score
    global beting_value
    while True:
        c1 = random.randint(2, 14)
        c2 = random.randint(2, 14)
        if c1 in (12, 13, 14):
            c1 = 10
        if c2 in (12, 13, 14):
            c2 = 10
        player = c1 + c2
        dc1 = random.randint(2, 14)
        dc2 = random.randint(2, 14)
        if dc1 in (12, 13, 14):
            dc1 = 10
        if dc2 in (12, 13, 14):
            dc2 = 10
        dealer = dc1 + dc2
        if player > 21 and c1 == 11 or c2 == 11:
            c1 = 1
        player = c1 + c2
        if dealer > 21 and dc1 == 11 or dc2 == 11:
            dc1 == 1
        player = c1 + c2
        dec = 0
        if dealer < 17:
            dec = random.randint(2, 14)
            if dec in (12, 13, 14):
                dec = 10
            dealer += dec
            if dealer > 21 and dec == 11:
                dec = 1
        player = c1 + c2
        if c1 == 10:
            face_card1 = random.randint(1, 4)
            if face_card1 == 1:
                face_card1 = 10
            if face_card1 == 2:
                face_card1 = "Jack"
            if face_card1 == 3:
                face_card1 = "Queen"
            if face_card1 == 4:
                face_card1 = "King"
        if c2 == 10:
            face_card2 = random.randint(1, 4)
            if face_card2 == 1:
                face_card2 = 10
            if face_card2 == 2:
                face_card2 = "Jack"
            if face_card2 == 3:
                face_card2 = "Queen"
            if face_card2 == 4:
                face_card2 = "King"
        pc1 = 10
        pc2 = 10
        ace = "Ace"
        if c1 in (1, 11):
            pc1 = str(ace)
        if c2 in (1, 11):
            pc2 = str(ace)
        if c1 != 10:
            pc1 = c1
        if c1 == 10:
            pc1 = str(face_card1)
        if c2 != 10:
            pc2 = c2
        if c2 == 10:
            pc2 = str(face_card2)

        beting_value = repeat_int(
            f"You currently have ${score}, how much will you bet? ")
        if beting_value > score:
            print("You don't have that much money, you bet $0 instead")
            beting_value = 0
        print(f"You got {pc1} and {pc2}")
        while True:
            horse = input(
                f'You got {player} total, type "h" to hit or type "s" to stand: ')
            if horse in ("h", "H"):
                ec = random.randint(2, 14)
                if ec in (12, 13, 14):
                    ec = 10
                if player + ec > 21 and ec == 11:
                    ec = 1
                player += ec
                print(f"you got another {ec}, your new total is {player}")
                time.sleep(1)
                if player >= 21:
                    higher_or_lower(dealer, player)
                    break
            elif horse in ("s", "S"):
                higher_or_lower(dealer, player)
                break
        if score <= 0:
            print("Your broke, you lose")
            time.sleep(2)
            return False
        return True


def play():
    global player
    global dealer
    global beting_value
    while True:
        player = 0
        dealer = 0
        beting_value = 0
        game = draw()
        save()
        if game == False:
            break
        ret = input("Will you return to the menu, yes(y) or no(n)? ")
        if ret in ("y", "Y"):
            print("Returning to menu")
            time.sleep(2)
            return False
        time.sleep(2)
        print("------------------")
