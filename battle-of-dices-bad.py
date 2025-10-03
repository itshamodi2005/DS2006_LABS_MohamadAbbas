import random

def rollD4():
    return random.randint(1, 4)

def rollD6():
    return random.randint(1, 6)

def rollD8():
    return random.randint(1, 8)

def rollD12():
    return random.randint(1, 12)

def rollD20():
    return random.randint(1, 20)

def rollD100():
    return random.randint(1, 100)

player1_score = 0
player2_score = 0
round_number = 0

while player1_score < 3 and player2_score < 3:
    round_number += 1
    print("Round", round_number)

    input("Player 1, press Enter to roll the dice...")
    dice1 = rollD6()
    print("Player 1 rolled:", int(dice1))

    input("Player 2, press Enter to roll the dice...")
    dice2 = rollD6()
    print("Player 2 rolled:", int(dice2))

    
    if dice1 > dice2:
        player1_score += 1
        print("Player 1 wins this round!")
    elif dice2 > dice1:
        player2_score += 1
        print("Player 2 wins this round!")
    else:
        print("It's a draw!")

    print("\nScores: Player 1 =", player1_score, ", Player 2 =", player2_score)

