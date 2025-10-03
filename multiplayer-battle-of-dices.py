import random
def rollD6():
    return random.randint(1, 6)

winning_score = 3
player_names = []
player_wins = []
player_roll_history = []

number_of_players = int(input("Enter number of players: "))

for i in range(number_of_players):
    name = input(f"Enter name of player {i + 1}: ")
    player_names.append(name)
    player_wins.append(0)

    player_roll_history = []

    for i in range(number_of_players):
        player_roll_history.append([])

gameover = False
rounds = 0

while gameover is False:
    print(f"Round {rounds + 1}")

    current_rolls = []

    for i in range(number_of_players):
        roll = rollD6()
        current_rolls.append(roll)
        player_roll_history[i].append(roll)
        print(f"{player_names[i]} rolled a {roll}")

    input("Press Enter to continue...")

    max_roll = max(current_rolls)

    Winners = []

    for j in range(number_of_players):
        if current_rolls[j] == max_roll:
            Winners.append(player_names[j])
            player_wins[j] += 1
    print(f"Winner(s) of this round: {Winners}")

    for z in range(number_of_players):
        if player_wins[z] >= winning_score:
            gameover = True
            print(f"{player_names[z]} has won the game!")
            break
    if gameover is False:
        print("Current Scores:")

    rounds += 1


filename = input("Enter the filename to save the results: ")
with open(filename, "w") as file:
    for round_number in range(rounds):
        file.write(f"Round {round_number+1}: ")
        rolls_str = ""  
        for i in range(number_of_players):
            rolls_str += (f"{player_names[i]} rolled {player_roll_history[i][round_number]}")
            if i < number_of_players - 1:
                rolls_str += ", "
        print(f"Saving {rolls_str}")
        file.write(rolls_str + "\n")
