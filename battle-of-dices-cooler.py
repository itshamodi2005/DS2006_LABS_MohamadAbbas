import random

def rollD6():
    return random.randint(1, 6)

def rollD12():
    return random.randint(1, 12)

player1_score = 0
player2_score = 0
round_number = 0

while player1_score < 3 and player2_score < 3:
    round_number += 1
    print("Round", round_number)

    input("Player 1, press Enter to roll the dice...")
    p1_dice1 = rollD6()
    p1_dice2 = rollD12()
    p1_total = p1_dice1 + p1_dice2
    print(f"Player 1 rolled: D6={p1_dice1}, D12={p1_dice2}, Total={p1_total}")

    input("Player 2, press Enter to roll the dice...")
    p2_dice1 = rollD6()
    p2_dice2 = rollD12()
    p2_total = p2_dice1 + p2_dice2
    print(f"Player 2 rolled: D6={p2_dice1}, D12={p2_dice2}, Total={p2_total}")

    if p1_total > p2_total:
        player1_score += 1
        print("Player 1 wins this round!")
    elif p2_total > p1_total:
        player2_score += 1
        print("Player 2 wins this round!")
    else:
        print("It's a draw!")

    print(f"Scores -> Player 1: {player1_score}, Player 2: {player2_score}\n")

if player1_score == 3:
    print(" GG player 1 you won! ")
else:
    print(" GG player 2 you won! ")
