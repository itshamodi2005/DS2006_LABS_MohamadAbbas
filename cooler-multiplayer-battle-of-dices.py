import random

def rollD6():
    return random.randint(1, 6)

def rollD12():
    return random.randint(1, 12)

winning_score = 3
player_names = []
player_wins = []
player_roll_history = []

number_of_players = int(input("Enter number of players: "))

for i in range(number_of_players):
    name = input(f"Enter name of player {i + 1}: ")
    player_names.append(name)
    player_wins.append(0)

for i in range(number_of_players):
    player_roll_history.append([])

gameover = False
rounds = 0

while not gameover:
    print(f"\nRound {rounds + 1}")

    current_totals = []

    for i in range(number_of_players):
        d6 = rollD6()
        d12 = rollD12()
        total = d6 + d12

        current_totals.append(total)
        player_roll_history[i].append((d6, d12, total))

        print(f"{player_names[i]} rolled D6={d6}, D12={d12}, Total={total}")

    input("Press Enter to continue...")

    max_roll = max(current_totals)
    winners = []

    for j in range(number_of_players):
        if current_totals[j] == max_roll:
            winners.append(player_names[j])
            player_wins[j] += 1

    print(f"Winner(s) of this round: {winners}")

    for z in range(number_of_players):
        if player_wins[z] >= winning_score:
            gameover = True
            print(f"{player_names[z]} has won the game!")
            break

    if not gameover:
        print("Current Scores:")
    rounds += 1

# --- Save results to file ---
filename = input("\nEnter the filename to save the results: ")
with open(filename, "w") as file:
    for round_number in range(rounds):
        file.write(f"Round {round_number+1}: ")
        rolls_str = ""  
        for i in range(number_of_players):
            d6, d12, total = player_roll_history[i][round_number]
            rolls_str += (f"{player_names[i]} rolled D6={d6}, D12={d12}, Total={total}")
            if i < number_of_players - 1:
                rolls_str += " | "
        file.write(rolls_str + "\n")
        print(f"Saving {rolls_str}")
